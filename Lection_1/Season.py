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