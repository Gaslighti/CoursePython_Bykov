# 3.	Создайте матрицы 8x4 и 4x2 и перемножьте, результирующую матрицу выведите в консоль.

import numpy as np

# Создаем матрицу 8x4 с рандомными значениями
matrix1 = np.random.random((8, 4))

# Создаем матрицу 4x2 с рандомными значениями
matrix2 = np.random.random((4, 2))

# Перемножаем матрицы
result_matrix = np.dot(matrix1, matrix2)

# Выводим результирующую матрицу в консоль
print("Результирующая матрица (8x2):")
print(result_matrix)
