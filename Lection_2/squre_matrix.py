# # Напишите функцию square_matrix, которая принимает квадратную матрицу
# # (список списков) и возвращает матрицу, где каждый элемент возведён в квадрат.
def square_matrix(list_of_list):
    new_sq_matrix = []
    for lst in list_of_list:
        new_lst = []
        for element in lst:
            new_lst.append(element ** 2)
        new_sq_matrix.append(new_lst)
    return new_sq_matrix


input_lst = [[1, 2], [3, 4], [5, 10, 3]]

print(square_matrix(input_lst))
