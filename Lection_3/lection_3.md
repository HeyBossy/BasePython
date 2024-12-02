# Особенности языка
## Как обрабатывать исключения в Python?
finally - в единственном числе. Он выполняется всегда.
ексепт отсуствует если есть финали, а финали отсувтует если есть ексепт.
Одновременно они не могут отсутсовать.
```python
# Как обрабатывать исключения в Python?
# Проще попросить прощения, чем разрешения
try:
# код, в котором потенциально может появиться исключение
    a = int(input('Делимое: '))
    b = int(input('Делитель: '))
    print(f'Частное: {a / b}')
except ZeroDivisionError:
# обработка исключения
    print('Делитель не может быть нулем')
except ValueError:
    print('Делимое и делитель должны быть числом')
else:
    print('Молодец, ты справился с вводом данных')
finally:
    print('Спасибо, что воспользовались нашим калькулятором')1234567891011121314
```
Несколько исключений
```python
try:
    a = int(input('Делимое: '))
    b = int(input('Делитель: '))
    print(f'Частное: {a / b}')
except (ZeroDivisionError, ValueError) as err:
    print(err)

```
# Контекстный менеджер
**Менеджер контекста** управляет входом в нужный контекст выполнения и выходом из него для выполнения
блока кода:
```python
with <выражение> [as <переменная>][, <выражение> [as <переменная>]]:
<блок_кода>
```
```python
try:
    f = open('/proc/cpuinfo')
    info = list(filter(lambda i: i.strip(), f))
finally:
    f.close()
```

Закрывает файл контексный менеджер
```python
with open('/proc/cpuinfo') as f:
    info = list(filter(lambda i: i.strip(), f))
```
Для контекста два метода :
1) __enter__() - вход в контекст и возвращение объекта
2)  __exit__() - выход из контекста
 ## Итераторы
За место фора типо

**Итератор** - это объект, который позволяет поочередно получать элементы коллекции.

Итератор в Python - это объект, который реализует **протокол итерации**: 
- __iter__() - возвращает объект-итератор
- __next__() - возвращает следующий элемент, или выбрасывает исключение StopIteration

Python предоставляет итераторы для: str, tuple, list, set, dict и д.р.

Python автоматически вызывает методы __iter__() и __next__() в цикле for

Что и как можно итерировать?
```python
product_name = 'Говорящий хомячок'
for c in product_name:
# Строки итерируются посимвольно
    print(c)
```
```python
hamster_names = ['Хома', 'Сеня', 'Роза', 'Соня']# hamster_names = ('Хома', 'Сеня', 'Роза', 'Соня')
# hamster_names = {'Хома', 'Сеня', 'Роза', 'Соня'}
for name in hamster_names:
# Списки, кортежи, множества
# итерируются по элементам
    print(name)
```
```python
for i, name in enumerate(hamster_names):
# Элементы можно пронумеровать
    print(f'Index: {i}, Value: {name}')
```
```python
product = {'name': 'Колесико', 'price': 1499.99, 'count': 10}
for i in product:
    # Словари итерируются по ключам
    print(i)# => 'name' 'price' 'count'
```

```python
for value in product.values():
    # Можно итерировать по значениям
    print(value)
```

```python
for key, value in product.items():
# Можно итерировать по ключам и значениям
print(f'{key}: {value}')
```

## Генераторы
**Генератор** - это функция, которая воспроизводит последовательность значений

Инструкция ``yield`` возвращает результат, и выполнение функции приостанавливается в этой точке:
```python
def generator():
    print('Шаг №1')
    yield 1
    print('Шаг №2')
    yield 2
    print('Шаг №3')
gen = generator() # Объект генератора создан123456789print(next(gen))
print(next(gen)) # Печатает 'Шаг №1' и возвращает 110print(next(gen))
print(next(gen)) # Печатает 'Шаг №2' и возвращает 211print(next(gen))
print(next(gen)) # Печатает 'Шаг №3' и выбрасывает исключение StopIteration12
```
Выполнение функции возобновляется с инструкции, следующей за ``yield``, когда метод ``__next__()`` будет вызван
снова 

Нет смысла использовать return - выйти из генератора return None
```text
| Характеристика      | Итератор                         | Генератор               |
|---------------------|-------------------------         |-------------------------|
| Создание            | Класс с методами                 | Функция с `yield`      |
| Состояние           | В атрибутах класса               | В локальных переменных   |
| Память              | Может использовать больше памяти | Использует меньше памяти |
```

```python 
from urllib.request import urlopen
def iter_pages(urls):
    """Генератор возвращает содержимое веб документов."""
    for url in urls:
        yield urlopen(url).read()
        
urls = ('https://python.org/', 'https://docs.python.org/3/')

for content in iter_pages(urls):
    print(content)
```
Для генераторов считается недопустимым по завершении итераций возвращать значение, отличное от None

# Декоратор 
Это  функция для  замыкание функций, про арги и кварги

**Декоратор** - это функция, основное назначение которой состоит в том, чтобы служить оберткой для другой
функции или класса:

**ПРИКОЛ В ТОМ ЧТО МЫ НЕ МЕНЯЕМ ОРИГИНАЛЬНУЮ ФУНКЦИЮ**

**Сначала делаем декоратор а потом оригниальная любая функция**

Обязательно входная переменная функция!! И возращает ссылку
```python 
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
Главная цель такого обертывания - изменить или расширить возможности обертываемого объекта

Чтобы применить декоратор к функции или методу, к имени декоратора добавляется символ @:

Перед деф нашей ставится @ и имя декоратора. Передать декоратору ссылку на  f.
```python 
@decorator
# f = decorator(f)
def f():
    pass
``` 
## Простой декоратор
```python
from functools import wraps
import time

def benchmark(func):
    '''декоратор (benchmark)- Сколько времени разная реализация идет'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''Функция обертка'''
        started = time.time() # время до
        result = func(*args, **kwargs) #  наша оригнинальная функция для подсчета чего-то
        worked = time.time() - started # время после
        template = 'Функция "{}" выполнилась за {:f} микросекунд'
        # выводим имя функции расчетной и получаем микросеки
        print(template.format(func.__name__, worked * 1e6))
        return result
    return wrapper # возращаем обертку сразу


@benchmark
def factorial(n):
    '''Оригинальная функция - факкториал + она обернута в декоратор'''
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

print(factorial(25)) # Функция "factorial" выполнилась за 7.867813 микросекунд
print(factorial(23)) # Функция "factorial" выполнилась за 5.483627 микросекунд
```
## Декораторы с параметрами
**Декоратор с параметрами** - это декоратор, который принимает дополнительные аргументы, позволяющие
настроить его поведение при применении к функции или методу:
```python
def decorator_factory(<параметры_декоратора>):
'''Хранит параметры декоратора типо'''
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
    
# факторы декоратора
@decorator_factory(<аргументы>)
# f = decorator_factory(<аргументы>)(f)
def f():
    pass
```

**Пример**
 Хотим получить данные с сайта но бывают задержки и ищем исключения.
```python
from functools import wraps
from random import random
from time import sleep

def retry_on_exception(max_retries=3, delay=1.0, exceptions=(Exception,)):
    """Декоратор, повторяющий выполнение функции при возникновении исключения."""
        def decorator(func): # декоратор
            @wraps(func)
            def wrapper(*args, **kwargs): # обертка
                retries = max_retries # максимальная попытка
                while retries > 0: # пока попытки больше нуля
                    try: # результат нашей функцией
                        return func(*args, **kwargs)
                    except exceptions:
                        # уменьшаем кол-во попыток
                        retries -= 1
                        if retries > 0:
                            sleep(delay)
                        else:
                            raise # подождали но если ты падаешь - пошел в жопу
            return wrapper
        return decorator
    
# Декоратор применяется к функции unstable_task, которая может вызывать исключение ValueError с вероятностью 70% (если случайное число меньше 0.7).
# При возникновении этого исключения функция будет автоматически повторять выполнение до 3 раз (или меньше, если вы измените параметр max_retries).
# если в функции, декорированной с помощью вашего декоратора retry_on_exception, возникает исключение, которое не указано в параметре exceptions, то это исключение будет выброшено, и программа завершит выполнение с ошибкой. 
@retry_on_exception(exceptions=(ValueError,)) # аргумент декоратора смотрим вальюерор только
def unstable_task():
    if random() < 0.7:
        raise ValueError('Fail')
```

Порядок применения и выполнения декораторов
```python
from functools import lru_cache, wraps
from urllib.request import urlopen
from time import sleep
def pause(seconds):
    """Декоратор выполняет функцию с задержкой в определенные секунды (параметры декоратора)."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs) # вызываем нашу функцию с задержкой
        return wrapper
    return decorator

@lru_cache
@pause(5)
def get_page(url):
    return urlopen(url).read()
# сначала обертка pause  а потом декоратор lru_cache - множество декораторов

print(get_page('http://python.org')) # применение наоборт.. сначала кеш (кеширует рез работы функции)  а потом тока пауза 
print(get_page('http://python.org'))
```

**wraps** - помогает сохранить информацию о функции, такую как её имя, документация и аннотации, после того как функция была обернута. Но его не обязательно применять..просто красиво типо