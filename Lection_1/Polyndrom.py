# Задача 3: Палиндром
# Проверить, является ли введенная строка или число палиндромом.

import re

polindrom = input("Введите строку или число: ")

# Удаление всех символов, кроме букв и цифр, и приведение к нижнему регистру
cleaned = re.sub(r'[^a-zA-Z0-9]', '', polindrom).lower()

# Проверка на палиндром
if cleaned == cleaned[::-1]:
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')

def is_polyndorm(cleaned_s):
    '''Проверка чисто по флагам'''
    left = 0
    right = len(cleaned) - 1
    output = True
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            output = False
            break
        left += 1
        right -= 1
    return output

print(f'Через флаги проверка: {is_polyndorm(cleaned)}')
