# Пользовательские функции
**Функция** - это блок кода, который можно вызывать многократнo
Функции это объект. Хранится в ОП.
```python
def <имя_функции>( [<аргументы>] ):
<тело_функции
```
В Python можно возвращать несколько значений
```python
from random import randrange
def random_color():
    """Возвращает случайный цвет в RGB."""
    return randrange(256), randrange(256), randrange(256)
print(random_color()) # (16, 108, 200)
print(random_color()) # вернул кортеж типо (180, 52, 24) 
```
**Значения аргументов по умолчанию**
Задаются дефолтные переменные через равно.
```python
from datetime import datetime
def format_current_datetime(fmt='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(fmt)
print(format_current_datetime()) # 2024-11-11 17:12:28
print(format_current_datetime('%A, %d %B %Y, %X')) # Monday, 11 November 2024, 15:14:39123456789
```
Аргументы по умолчанию задаются только после обязательных!!!

по умолчанию моожно не задавать явно.
```python
def prompt(msg, default=None):
    value = input(f'{msg}: ')
    return value if value else default

lastname = prompt('Фамилия')
firstname = prompt('Имя')
middlename = prompt('Отчество', '')
```
## Передача аргументов изменяемого типа
**Нельзя использовать  аргументы по умолчанию - изменяемые!! (изменяемые - все кроме кортежей и скаляров)**
Но например:
```python
import re
# -> None - возращаемый тип данных

def find_words(text: str, output: list[str]) -> None:
    """Разбивает текст на слова и результат записывает в аргумент output."""
    output.extend(
    re.findall(r'''\b\w+(?:['-]\w+)*\b''', text.lower())
    )
    
src = "Special cases aren't special enough to break the rules."
words = []
find_words(src, words)

# ['special', 'cases', "aren't", 'special', 'enough', 'to', 'break', 'the', 'rules']
print(words)
```
```words``` - ссылается на список. ```output``` ссылается на тот же список - изменяемый тип. Одно и то же в памяти. Сначала  ```words``` пустой, а потом после функции стал уже не пустой.

Еще пример почему это плохо.
```python
import re
def find_words(text: str, output: list[str] = []) -> list[str]:
    """Разбивает текст на слова и результат записывает в аргумент output."""
    output.extend(
    re.findall(r'''\b\w+(?:['-]\w+)*\b''', text.lower())
    )
    return output

print(find_words('First call')) # ['first', 'call']
print(find_words('Second call')) # ['first', 'call', 'second', 'call']
# НЕ УБИРАЕТ СТАРЫЕ ЗНАЧЕНИЯ!! ДОЛЖЕН ПРОСТО БЫТЬ Second call
```
Как переписать?

Лучше когда изменяемый тип то инициализировать в ```None.```

```python
import re
def find_words(text: str, output: list[str] | None = None) -> list[str]:
    """Разбивает текст на слова и результат записывает в аргумент output."""
    if output is None:
        output = []
    
    output.extend(
    re.findall(r'''\b\w+(?:['-]\w+)*\b''', text.lower())
    )
    return output
```

## Позиционные и именованные аргументы
к аргументам можно обращаться по именам - именновые
позиционные - без имен. Строгая позиция
```python
def rgb2hex(red, green, blue):
    pass

black = rgb2hex(0, 0, 0) # как позиционные

dark_red = rgb2hex(red=139, green=0, blue=0) # как именованные
white = rgb2hex(blue=255, green=255, red=255) # в любом порядке

dark_blue = rgb2hex(0, 0, blue=139) # как смешанные
dark_green = rgb2hex(0, green=139, 0) # ошибка! ток последнтй элемент можно
dark_green = rgb2hex(0, 0, green=139) # ошибка! - грин только на втором местеЁЁ
```
- / - все аргументы которые слева - позиционные. после слеша передавай как хочешь
 - * звездочка. Это не аргумент. А синтаксис. Все что идет после звездочки можно передать только как именнованный аргумент, но не как позиционный
```python
# Python >= 3.8
# слеш
def rgb2hex(red, green, blue, /, hash=True):
    pass

black = rgb2hex(0, 0, 0) # OK
dark_red = rgb2hex(red=139, green=0, blue=0) # ошибка!

# звездочка
def rgb2hex(red, green, blue, *, hash=True):
    pass

black = rgb2hex(0, 0, 0, False) # ошибка!
dark_red = rgb2hex(139, 0, 0, hash=False) # OK
```
## Переменное количество  позиционных!! аргументов
### args
```*args``` - любое количество **позиционных** аргументов (это кортеж)

```python
def multi(a, b, *args):
    """Возвращает произведение двух и более чисел."""
    r = a * b
    for i in args:
    r *= i
    return r

print(multi(1, 2)) # 2
print(multi(1, 2, 3, 4, 5)) # 3, 4, 5 - кортеж аргс
```
```python
from configparser import ConfigParser
import os

def make_config(*config_files):
    """Читает конфигурационные файлы и возвращает объект ConfigParser."""
    config = ConfigParser() # класс
    config.read(config_files) # рид - читает файлы
    return config

config = make_config('/etc/app/config.ini',
os.path.expanduser('~/.config/app/config.ini'))
```
## Переменное количество  именованных!! аргументов
**kwargs** - это словарь - ключи - имена, значения - значения
```python
def db_connect(provider, /, **kwargs):
    """Возвращает объект соединения с БД."""
    print('Connectiong to database', provider)
    print('==>', kwargs)
    
db_connect('sqlite', filename='db.sqlite')
db_connect('mysql', user='root', passwd='toor', db='db', charset='utf-8')
```

```python
def render_template(template_name_or_list, **context):
        """Отрисовывает шаблон по имени с заданным контекстом."""
    render_template('product.html', title='Колесико', price=1499.99, count=10)
    
render_template(
        'index.html',
        products=[
        {'name': 'Колесико', 'price': 1499.99, 'count': 10},
        {'name': 'Домик', 'price': 3499.99, 'count': 3},
        ],
)
```
## Как развернуть кортеж/список  в значения позиционных аргументов
```python
numbers = (1, 2, 3, 4, 5)
def multi(a, b, *args):
    """Возвращает произведение двух и более чисел."""
    r = a * b
    for i in args:
    r *= i
    return r

print(
multi(*numbers) # - 5 позиционных аргументов
# 120
)

hamster_names = ['Хома', 'Сеня', 'Роза', 'Соня']
print(*hamster_names, sep=', ') # Хома, Сеня, Роза, Соня

# Лучше использовать метод строк join
print(', '.join(hamster_names)) # Хома, Сеня, Роза, Соня

# range - это итератор
even_numbers = range(2, 11, 2)
print(
multi(*even_numbers) # 3840
)
```
# Как развернуть словарь в значения именованных аргументов?
```python
provider = 'postgres'
options = {
'user': 'root',
'password': 'toor',
'host': 'localhost',
'database': 'db',
}
db_connect(provider, **options)
```
 # Какие бывают функции?
## Анонимная функция 
функция обратного вызова. передаем в качестве аргумента в другую функцию

Пример: филтер, мап
```python
numbers = list(range(10))

# Список квадратов чисел - [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = list(map(lambda x: x ** 2, numbers))

# Список не четных чисел - [1, 3, 5, 7, 9]
odd = list(filter(lambda i: i % 2, numbers))
```
## Рекурсивная функция
**Прямая рекурсия** - функция в своем теле вызывает сама себя:
```python
# Пример факториал
def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)

print(f'Факториал 5 = {factorial(5)}')
```
**Косвенная рекурсия** - функция в своем теле вызывает другую функция, которая в свою очередь вызывает
первую:
```python
def func_a():
    func_b()

def func_b():
    func_a()
```
# Область видимости и время жизни переменной
 Каждая функция создает области видимости - там все переменные будут существовать в области видимости функции.

Переменные функции работают пока работает функция
 
Глобальные функции работают пока работает программа.
```python
# Глобальная переменная
global_var = 'Глобальная переменная модуля'

def f(arg):
    # Локальная переменная для функции f
    f_scope_var = 0
    
    def inner(inner_arg):
        # Локальная переменная для вложенной функции inner
        inner_scope_var = ''
        
        # Доступ к глобальной и локальной переменным
        print(global_var, f_scope_var)  # Печатает глобальную и локальную переменную f
        
        global global_var  # Указывает, что мы хотим использовать глобальную переменную
        nonlocal f_scope_var  # Указывает, что мы хотим использовать f_scope_var из внешней функции
        
        f_scope_var += 1  # Изменяем значение f_scope_var

    inner(10)  # Вызываем вложенную функцию

# Вызовем функцию f
f(5)
```
# Замыкания

**Замыкание** - это функция, которая "запоминает" окружение, в котором она была создана, даже если оно больше
не доступно напрямую

Замыкание даёт вам доступ к области видимости внешней функции из внутренней функции:

```python
def trim(chars=None):
    """Удаляет указанные символы с начала и с конца строки."""
    def inner(s):
    return s.strip(chars)
    return inner


spaces_trim = trim() # функция удаляет любые пробельные символы
slashes_trim = trim('/|\\') # функция удаляет любые слеши

email = input('E-Mail: ') # " user@example.com "
email = spaces_trim(email) # user@example.com

slashes_trim('/string/with/slashes/') # string/with/slashes

```