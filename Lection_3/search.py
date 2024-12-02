# pretty print
# поиск подстроки в файле и ее задача вернуть в какой строке
# была найдена данная подстрока
# Вывод: кортеж: номер строки и строка целиком


from pprint import pprint
def search_hard(filename, sub):
    results = []
    # r - read file
    # w - write file
    # a - дописать в конце файла
    # w+ -  перезаписывать файлы
    # t - text filename and b - binary file (rb for example)
    f = open(filename, 'r') #функция открывает файл
    try:
        for i, line in enumerate(f, start=1):
            # построчно итерируем файл и получаем номер строки в файле
            if sub.lower() in line.lower():
                results.append((i, line))
    finally:
        # Нужно закрыть файл!
        f.close()

    return results
def search_in_file(filename, sub):
    with open(filename) as file:
        # generator
        for i, line in enumerate(file, start=1):
            if sub.lower() in line.lower():
                yield i, line.strip()


# модуль а не исполняемый файл
if __name__ == '__main__':
    # ищем файлы
    # find_file = search_hard(__file__, 'вывод') # file - путь к текущему файлу
    generator = search_in_file(__file__, 'вывод')
    find_file = list(generator) # вывод генератора надо оборачивать!!!!
    print(find_file)

#  дз сделать енумерейт через генератора и мап через генератора и аналог фильтра через генератора