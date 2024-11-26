# Задача 1: Времена года
# Попросить пользователя ввести с клавиатуры номер месяца (проверка корректности ввода не требуется).
# Определить и вывести на экран время года: winter, spring, summer, autumn.

month = int(input('Введите номер месяца: '))
dct_month = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}

output = None
for season, months in dct_month.items():
    # Проверяем, входит ли номер месяца в список
    if month in months:
        output = season
        print(f'Ваш месяц: {output}')
        break

if output is None:
    print('Введите корректный номер месяца')

############### Код преподавателя
seasons_tuple = ('winter', 'spring', 'summer', 'autumn')
is_valid = False

# Этот цикл будет выполняться, пока is_valid равно False
while not is_valid:
    month = input('Введите номер месяца еще раз: ')

    # Check if input is a digit
    if month.isdigit():
        number = int(month)
        # Check if the number is within the valid range
        if 1 <= number <= 12:
            is_valid = True
        else:
            print('Введите число от 1 до 12.')
    else:
        print('Введите корректное значение.')

index_month = number % 12 // 3
print(f'Сезон: {seasons_tuple[index_month]}')
