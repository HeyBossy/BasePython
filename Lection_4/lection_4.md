# Классы и объекты
## Как создать класс в Python?
**Класс** - это шаблон для создания объекта (экземпляра):

каждое слово с заглавной буквы - класс, а через _ это функция
```python
class <ИмяКласса>:
    <тело_класса>
    
obj1 = <ИмяКласса>()
obj2 = <ИмяКласса>()
obj3 = <ИмяКласса>()
```

**Класс** - это набор данных и методов, имеющих общую, целостную, хорошо определенную сферу ответственности:
```python
class Singer:
    pass

avril_lavigne = Singer()
lilaya = Singer()
```
## Как объявить метод класса?
В Python **метод** - это функция, объявленная в теле класса:

кароче метод это функция
```python
class Singer:
    def __init__(self, name, website):
        pass
   
    def get_name(self):
        pass
    
    def get_website(self):
        pass
```
 ```self ```- ссылка на текущий объект. ЧТОБЫ ОБРАТИТЬСЯ К ОБЪЕКТУ!!Не считается за переменную.
 
```__init__``` - конструктор, вызывается автоматически при создании объекта и выполняет инициализацию объекта
```python
avril_lavigne = Singer('Avril Lavigne', 'https://avrillavigne.com/')
lilaya = Singer('Лилая', 'https://music.yandex.ru/artist/11229116')12
```
В ООП методы **задают поведение объекта**
## Как объявить свойство класса?
В Python **свойство** - это переменная, которая принадлежит объекту и объявляется в конструкторе класса (инит):
```python
class Singer:
    def __init__(self, name, website):
        # это свойство
        self.name = name
        self.website = website
        self.albums = []
    
    def add_album(self, album):
        self.albums.append(album)
    
    def get_name(self):
        return self.name
    
    def get_website(self):
        return self.website
```
В ООП свойства - это **данные** объекта

Термины-синонимы: атрибуты, поля, данные, свойства-члены
## Что такое наследование?
**Наследование** - это механизм, позволяющий описать новый класс на основе уже существующего класса:
```python
class Validator:
    def __init__(self, message: str) -> None:
        self.error_message = message
    
    def validate(self, value: str) -> None:
        raise NotImplementedError

# RequiredValidator - ребенок а Validator - родитель
class RequiredValidator(Validator):
    def validate(self, value: str) -> None:
        if not value:
            raise ValueError(self.error_message)

validator = RequiredValidator(message='Требуется указать имя')
name = input('Введите имя: ')

try:
    validator.validate(name)
except ValueError as err:
    print(err)
```
## Как вызвать родительский метод?
**Переопределяя метод родителя** в дочернем классе, вызов родительского метода позволяет сохранить
существующую логику родителя и дополнить её новой

super().__init__ - вернет родительский конструктор, а то без -  мы затираем конструктор родительский
```python
class Validator:
    def __init__(self, message: str) -> None:
        self.error_message = message
        
        
class IntValidator(Validator):
    def __init__(
    self,
    message: str,
    min_value: int | None = None,
    max_value: int | None = None,
    ) -> None:
        super().__init__(message)
        self.min_value = min_value
        self.max_value = max_value
```
## Как объявить статическое свойство или метод?
**Статическое свойство** - это переменная, которая принадлежит классу и объявляется в теле класса

принадлежит классу!

К статическому свойству или методу можно получить доступ не создавая экземпляра:

classmethod - декортаор для статического метода

грубо говоря глобальная переменая)
```python
class Example:
    static_property = 0 #до def __init__  - для всех будет
    
    @classmethod
    def static_method(cls): # cls - ссылка на класс
        cls.static_property += 1 # Доступ к статическому св-ву из статического метода
    
    def method(self):
        self.static_property -= 1 # Доступ к статическому св-ву из метода

print(Example.static_property)# Доступ к статическому св-ву из клиентского кода
Example.static_method() # Доступ к статическому методу из клиентского кода12345678910111213
```
## Примеры использования "статики"
```python
class Validator:
    default_error_message = 'Invalid value.' # статическое свойство - до инита типо
    
    def __init__(self, error: str = '') -> None:
        self.error_message = error or self.default_error_message12345
```
```python
import json
    class Singer:
    def __init__(self, name, website):
        self.name = name
        self.website = website
        self.albums = []
    
    def add_album(self, album):
        self.albums.append(album)
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        obj = cls(data['name'], data['website'])
        
        for album in data.get('albums', []):
            obj.add_album(album)
        return obj
```

Разница между обычными переменными и статическими переменными в классе заключается в том, как они хранятся и к каким данным они имеют доступ. Давайте рассмотрим это подробнее.
Обычные переменные (экземплярные переменные)

    Что это? Обычные переменные создаются для каждого экземпляра (объекта) класса. Это значит, что каждый объект имеет свои собственные копии этих переменных.
    Доступ: Чтобы получить доступ к обычной переменной, вам нужно создать экземпляр класса. Эти переменные могут хранить данные, специфичные для каждого объекта.
    Пример:

    python
    class Car:
        def __init__(self, color):
            self.color = color  # Обычная переменная

    car1 = Car("red")   # car1 имеет свою собственную переменную color
    car2 = Car("blue")  # car2 имеет свою собственную переменную color
    print(car1.color)  # Вывод: red
    print(car2.color)  # Вывод: blue

Статические переменные

    Что это? Статические переменные принадлежат классу в целом, а не конкретному экземпляру. Это значит, что они общие для всех объектов этого класса.
    Доступ: Вы можете получить доступ к статическим переменным через имя класса, и они будут одинаковыми для всех экземпляров.
    Пример:

    python
    class Car:
        count = 0  # Статическая переменная

        def __init__(self, color):
            self.color = color
            Car.count += 1  # Увеличиваем счетчик при создании нового объекта

    car1 = Car("red")
    car2 = Car("blue")
    print(Car.count)  # Вывод: 2 (количество созданных объектов)

Обычные методы: Используются для работы с данными конкретного объекта. Например, если у вас есть машина с определённым цветом, вы можете использовать обычный метод для получения этого цвета.

Статические методы: Используются для выполнения задач, которые не зависят от состояния объекта. Например, если вам нужно сложить два числа, это не требует создания машины или другого объекта