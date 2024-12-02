def say_hello():
    return 'hello'
def greeting_username(firstname, lastname):
    '''Функция с аргументами'''
    return f'Hello, {firstname} {lastname}'
def null_decorator(func):
    '''Принимает ссылку на функцию.Добавляем "!"'''
    return func # НЕЛЬЗЯ func() + '' - ретерн будет уже не функция!!!

def exclaim_decorator(func):
    '''Всегда добавляем воскл знак '''
    def wrapper(*args, **kwargs):
        '''Любое количество позиционных аргументов для wrapper'''
        '''И развернули арги и кварги'''
        return func(*args, **kwargs) + '!'
    return wrapper # без () вызова

print(f'first func  say_hello: {say_hello} \n')

print(f'переназвали что стало с say_hello: {say_hello}')
say_hello = null_decorator(say_hello) # переназываем
print(f'\n {say_hello} одна и та же функция!! из-за нул декоратора')

say_hello = exclaim_decorator(say_hello) # переназываем
print(f'\n функция wrapper locals: {say_hello}') #locals - область видимости декоратора
print(f' \n получаем "!" для say_hello функции  - {say_hello()}')

print(f' --------\n Новая функция с двумя аргументами greeting_username ----------')
greeting_username = exclaim_decorator(greeting_username)
# greeting_username = exclaim_decorator(greeting_username) - два воскл знака
print(f' \n получаем  для greeting_username !  \n - {greeting_username(1, 2)}') # у врапера не 2 аргумента..ошибка а say_hello - 0. надо универсальную (арги и кварги для любого количества аргументов)
print(f'\n  С аргами и квагами стало для say_hello: \n {say_hello()}')
# у каждого своя область видимости