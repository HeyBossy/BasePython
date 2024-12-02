# Требуется реализовать две функции для работы с шифром Цезаря.
#
# Напишите функцию encode(s, rotn), которая принимает два аргумента: исходный текст и значение сдвига,
# выполняет кодирование и возвращает закодированный текст.
#
# Напишите функцию decode(s, rotn), которая принимает два аргумента: закодированный текст и значение сдвига,
# выполняет декодирование и возвращает оригинальный текст.
#
# Кодируются только буквы алфавита, числа, символы пунктуации и другие символы не кодируются.
#
# Сдвиг - это целое число, он цикличен и его максимальное значение равно количеству букв алфавита.
# В задаче используется только латинский алфавит,
# поэтому значение сдвига может быть от 0 до 25 (всего 26 символов).
#
# Нужно учитывать регистр символов, a со смещением 1, возвращает b, а A - возвращает B.
#
# В решении задачи вам пригодятся строковые функции/методы вашего ЯП, а также функции для работы с ASCII-кодами символов.
#
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

#encode
def encode(s, shift):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = lower_alphabet.upper()

    result = []
    for char in s:
        if char in lower_alphabet:  # Для строчных букв
            #  нужно сдвинуть буквы в алфавите (от 0 до 25).
            new_char = lower_alphabet[(lower_alphabet.index(char) + shift) % 26]
        elif char in upper_alphabet:  # Для заглавных букв
            new_char = upper_alphabet[(upper_alphabet.index(char) + shift) % 26]
        else:
            new_char = char  # Остальные символы не меняются
        result.append(new_char)
    return ''.join(result)

def decode(s, rotn):
    # Декодирование — это кодирование с отрицательным сдвигом
    return encode(s, -rotn)

original_text = "Hello, World!"
shift = 3

# Кодирование
encoded_text = encode(original_text, shift)
print(f"Encoded: {encoded_text}")  # Encoded: Khoor, Zruog!

# Декодирование
decoded_text = decode(encoded_text, shift)
print(f"Decoded: {decoded_text}")  # Decoded: Hello, World!