from abc import ABC, abstractmethod  # Импортируем абстрактные базовые классы и декоратор для абстрактных методов
from typing import Any  # Импортируем тип Any для универсальных аргументов и возвращаемых значений
from urllib.request import urlopen  # Для запросов к API (лучшше requset.get)
from urllib.parse import urlencode  # Для кодирования параметров в URL
import json  # Для работы с JSON-форматом
from dataclasses import dataclass  # Для создания dataclass-ов, удобных классов для хранения данных
from typing import Union


@dataclass  # Это датакласс, который автоматически генерирует методы __init__, __repr__, __eq__ и другие для хранения данных.
class WeatherInfo:
    """
    Класс для представления информации о погоде.

    Атрибуты:
        temperature (float): Температура.
        feels_like (float): Ощущаемая температура. Если не задана, используется температура.
        description (str): Описание погоды.
        wind (float): Скорость ветра. По умолчанию -1.
        wind_deg (float): Направление ветра в градусах. По умолчанию -1.
        pressure (float): Давление. По умолчанию -1.
        humidity (int): Влажность. По умолчанию -1.
    """
    temperature: float
    feels_like: Union[float, None] = None  # Может быть None, если не задано.
    description: str = ''
    wind: float = -1  # По умолчанию -1
    wind_deg: float = -1
    pressure: float = -1
    humidity: int = -1

    def __post_init__(self):
        """
        Метод для автоматического заполнения отсутствующих данных после инициализации.
        """
        if self.feels_like is None:
            self.feels_like = self.temperature

    def get_wind_direction(self) -> str:
        """
        Возвращает направление ветра в текстовом формате.

        Returns:
            str: Направление ветра.
        """
        directions = (
            "С", "ССВ", "СВ", "В", "ВЮВ", "ЮВ", "ЮЮВ",
            "Ю", "ЮЮЗ", "ЮЗ", "ЗЮЗ", "З", "ЗСЗ",
            "СЗ", "ССЗ", "С"
        )
        index = round(self.wind_deg / 22.5) % 16
        return directions[index]


class WeatherError(Exception):
    """
    Исключение для обработки ошибок, связанных с погодой.
    """
    pass


class WeatherProvider(ABC):
    """
    Абстрактный базовый класс для поставщиков данных о погоде.
    Просто типо архитектура с функциями без реализации типо.
    Это абстрактный класс, который требует, чтобы все его наследники реализовывали метод `get_weather`.
    """

    @abstractmethod
    def get_weather(self, city: str) -> WeatherInfo:
        """
        Абстрактный метод для получения погоды. ХЗ как делает но мы задали желаемоге поведение

        Args:
            city (str): Название города.

        Returns:
            WeatherInfo: Информация о погоде.
        """
        pass

    def _call_api(self, url: str, **parameters: Any) -> Any:
        """
        Вспомогательный метод для вызова API. ОН ЗАКРЫТЫЙ ИЗ_ЗА ДЕФИСА В НАЧАЛЕ  эти методы не должны использоваться вне класса

        Args:
            url (str): Базовый URL API.
            **parameters: Параметры для запроса.

        Returns:
            Any: Ответ от API в виде объекта Python (например, JSON).
        """
        qs = urlencode(parameters)
        with urlopen(f'{url}?{qs}') as resp:
            if 'application/json' in resp.headers.get('Content-Type', ''):
                return json.load(resp)
            return resp.read().decode()


class OpenWeatherMap(WeatherProvider):
    """
    Поставщик погоды через API OpenWeatherMap.
    """
    API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key: str) -> None:
        """
        Инициализирует поставщика с ключом API.

        Args:
            api_key (str): API ключ для доступа к OpenWeatherMap.
        """
        self.api_key = api_key

    def get_weather(self, city: str) -> WeatherInfo:
        """
        Получает данные о погоде для заданного города.

        Args:
            city (str): Название города.

        Returns:
            WeatherInfo: Объект с данными о погоде.
        """
        data = self._call_api(
            self.API_BASE_URL,
            appid=self.api_key,
            q=city,
            lang='ru',
            units='metric'
        )
        description = [i['description'] for i in data['weather']]
        return WeatherInfo(
            temperature=data['main']['temp'],
            feels_like=data['main'].get('feels_like'),
            description=', '.join(description),
            wind=data['wind']['speed'],
            wind_deg=data['wind']['deg'],
            pressure=round(data['main']['pressure'] * 0.75),
            humidity=data['main']['humidity']
        )


class WeatherApi(WeatherProvider):
    """
    Поставщик погоды через API WeatherApi.
    """
    API_BASE_URL = 'https://api.weatherapi.com/v1/current.json'

    def __init__(self, api_key: str) -> None:
        """
        Инициализирует поставщика с ключом API.

        Args:
            api_key (str): API ключ для доступа к WeatherApi.
        """
        self.api_key = api_key

    def get_weather(self, city: str) -> WeatherInfo:
        """
        Получает данные о погоде для заданного города.

        Args:
            city (str): Название города.

        Returns:
            WeatherInfo: Объект с данными о погоде.
        """
        data = self._call_api(
            self.API_BASE_URL,
            key=self.api_key,
            q=city,
            lang='ru',
            units='metric'
        )
        current = data['current']
        return WeatherInfo(
            temperature=current['temp_c'],
            feels_like=current['feelslike_c'],
            description=current['condition']['text'],
            wind=round(current['wind_kph'] / 3.6, 1),
            wind_deg=current['wind_degree'],
            pressure=round(current['pressure_mb'] * 0.75),
            humidity=current['humidity'],
        )


# Использование
service1 = OpenWeatherMap('1f5ca819fa6005b26a222541d0d94e49')
service2 = WeatherApi('ba5f017d63fd4cc5ad6150956240912')
weather1 = service1.get_weather('Санкт-Петербург')
weather2 = service2.get_weather('Санкт-Петербург')
print(f' Получаем погоду через OpenWeatherMap: {weather1}\n') # Получаем погоду через OpenWeatherMap: WeatherInfo(temperature=-1.08, feels_like=-5.61, description='пасмурно', wind=4, wind_deg=320, pressure=776, humidity=88)

print(f' Получаем погоду через WeatherApi: {weather2}') # Получаем погоду через WeatherApi: WeatherInfo(temperature=-0.6, feels_like=-2.5, description='Пасмурно', wind=1.5, wind_deg=288, pressure=776, humidity=86)

