# 7.	напишите функцию которая
# a.	принимает
# i.	вектор A длинной X
# ii.	размер слоя S - натуральное число
# iii.	Булевый параметр last - по умолчанию False
# b.	генерируется случайную матрицу B размером SxX
# c.	создайте новую матрицу - произведение вектора A и матрицы B
# d.	Найдите сумму каждой строки результирующей матрицы - должен получится вектор размером S
# e.	Результирующий вектор проходит через функцию:
# i.	Если last == False то функция - np.sin(x)
# ii.	иначе np.maximum(x, 0)
# f.	Вернуть результирующий массив и рандомную матрицу сгенерированную в начале функции,
# g.	Для теста вызовите функцию 3 раза:
# i.	первый - длинна вектора 5, заполнен случайными числами. Размер слоя 10
# ii.	второй - на вход передайте вектор из предыдущего запуска. Размер слоя 10
# iii.	третий - на вход передайте вектор из второго запуска, размер слоя 5 и last = True. Значения результата переведите в проценты и выведите в консоль.


import numpy as np

def process_vector(A, S, last=False):
    # Reshape A to handle both vectors and matrices
    if A.ndim == 1:
        A = A.reshape(-1, 1)  # Convert 1D array to a column vector

    # Generate a random matrix B of size SxX
    B = np.random.random((S, A.shape[0]))

    # Compute the result matrix as the dot product of B and A
    result_matrix = np.dot(B, A)

    # Compute the sum along the appropriate axis based on input type
    if A.ndim == 1:
        result_vector = np.sum(result_matrix, axis=1)
    else:
        result_vector = np.sum(result_matrix, axis=0)

    # Apply the specified function to the result vector
    if not last:
        result_vector = np.sin(result_vector)
    else:
        result_vector = np.maximum(result_vector, 0)

    return result_vector, B

# Test calls
vector1 = np.random.random(5)
layer_size1 = 10
result1, B1 = process_vector(vector1, layer_size1)

layer_size2 = 10
result2, B2 = process_vector(result1, layer_size2)

layer_size3 = 5
last_param = True
result3, B3 = process_vector(result2, layer_size3, last_param)

# Convert result3 to percentages and print
result3_percent = result3 * 100
print("Result of the third call in percentages:")
print(result3_percent)











