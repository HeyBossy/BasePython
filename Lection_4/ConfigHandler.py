# Реализовать простое средство для считывания и записи информации из конфигурационных файлов. Количество форматов не ограничено.
from abc import ABC, abstractmethod
from typing import Any
import json
import pickle


class ConfigHandler(ABC):
    """базовый абстрактный класс"""

    @abstractmethod
    def add(self, name: str, value: Any) -> None:
        """добавляет новый, или затирает существующий, параметр с именем name и указанным значением value"""
        pass

    @abstractmethod
    def get(self, name: str) -> Any:
        """ возвращает значение параметра с указанным именем"""
        pass

    @abstractmethod
    def all(self) -> dict[str, Any]:
        """ возвращает значения всех опций в виде словаря (можно генератора)"""
        pass

    @abstractmethod
    def delete(self, name: str) -> None:
        """удаляет значение опции с указанным именем"""
        pass

    @abstractmethod
    def clear(self) -> None:
        """удаляет значения всех опций (очистка)"""
        pass

    @abstractmethod
    def read(self, filepath: str) -> None:
        """абстрактный метод, выполняет чтение параметров из конфигурационного файла"""
        pass

    @abstractmethod
    def write(self, filepath: str) -> None:
        """абстрактный метод, записывает параметры в конфигурационный файл"""
        pass


class JsonConfigHandler(ConfigHandler):
    """Реализует операции чтения и записи в формате JSON."""

    def __init__(self):
        self.config = {}

    def add(self, name: str, value: Any) -> None:
        """добавляет новый, или затирает существующий, параметр с именем name и указанным значением value"""
        if name not in self.config:
            self.config[name] = value
        else:
            print('Имя уже есть')

    def get(self, name: str) -> Any:
        """ возвращает значение параметра с указанным именем"""
        return self.config.get(name)

    def all(self) -> dict[str, Any]:
        """ возвращает значения всех опций в виде словаря (можно генератора)"""
        return self.config

    def delete(self, name: str) -> None:
        """удаляет значение опции с указанным именем"""
        if name in self.config:
            del self.config[name]
        else:
            print('Не найдено имя у конфига')

    def clear(self) -> None:
        """удаляет значения всех опций (очистка)"""
        self.config.clear()

    def read(self, filepath: str) -> None:
        """абстрактный метод, выполняет чтение параметров из конфигурационного файла"""
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, filepath: str) -> None:
        """абстрактный метод, записывает параметры в конфигурационный файл"""
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(self.config, file)


class PickleConfigHandler(JsonConfigHandler):
    def __init__(self):
        super().__init__()

    def read(self, filepath: str) -> None:
        """абстрактный метод, выполняет чтение параметров из конфигурационного файла"""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
            print(f'Данные, прочитанные из PICKLE файла:\n{data}')

    def write(self, filepath: str) -> None:
        """абстрактный метод, записывает параметры в конфигурационный файл"""
        with open(filepath, 'wb') as f:
            pickle.dump(self.config, f)


if __name__ == '__main__':
    print('=====JsonConfigHandler=====\n')
    handler = JsonConfigHandler()

    print('Добавляем параметры\n')
    handler.add("host", "localhost")
    handler.add("port", 8080)

    print('Сохраняем параметры в файл\n')
    handler.write("config.json")

    print('Читаем параметры из файла\n')
    handler.read("config.json")

    print('Получаем все параметры\n')
    print(handler.all())  # {'host': 'localhost', 'port': 8080}

    print('Удаляем параметр\n')
    handler.delete("host")

    print('Очищаем все параметры\n')
    handler.clear()
    print(handler.all())

    print('\n=====PickleConfigHandler===========\n')
    pickle_handler = PickleConfigHandler()

    print('Добавляем параметры\n')
    pickle_handler.add("host", "127.0.0.1")
    pickle_handler.add("port", 9090)

    print('Сохраняем параметры в файл\n')
    pickle_handler.write("config.pkl")

    print('Читаем параметры из файла\n')
    pickle_handler.read("config.pkl")

    print('Получаем все параметры\n')
    print(pickle_handler.all())  # {'host': '127.0.0.1', 'port': 9090}

    print('Удаляем параметр\n')
    pickle_handler.delete("host")
    print(pickle_handler.all())  # {'port': 9090}

    print('Очищаем все параметры\n')
    pickle_handler.clear()
    print(pickle_handler.all())  # {}
