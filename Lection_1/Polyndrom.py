# Задача 3: Палиндром
# Проверить, является ли введенная строка или число палиндромом.

import re

polindrom = input("Введите строку или число: ").lower()

# Удаление всех символов, кроме букв и цифр, и приведение к нижнему регистру
cleaned = re.sub(r'[^a-zA-Z0-9]', '', polindrom)
#  можно isalnum - Возвращает флаг, указывающий на то, содержит ли строка только цифры и/или буквы.
letters = (list(filter(lambda i: i.isalnum(), polindrom)))

# другой варик проверить только до середины
is_poly = True
for i in range(len(cleaned)//2):
    if letters[i] != letters[-1-i]:
        is_poly = False
        break
print('yes' if is_poly else 'no')

# Проверка на палиндром мое
if cleaned == cleaned[::-1]:
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')


# Проверка на палиндром через флаги
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
