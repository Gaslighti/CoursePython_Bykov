# 5.	Создайте функцию, которая
# a.	принимает число (количество элементов в матрице)
# b.	Проверяет можно ли построить матрицы с размерностью из множителей принимаемого числа.
# c.	При проверке не учитывать матрицы с множителем “1”
# d.	постройте все возможные матрицы и выведите в консоль.
# e.	если число нельзя разбить на множители без остатка выведите сообщение в консоль.
import numpy as np


def generate_matrices(num_elements):
    # Функция для получения всех возможных множителей числа (исключая 1)
    def get_factors(num):
        factors = []
        for i in range(2, num):
            if num % i == 0:
                factors.append(i)
        return factors

    # Получаем множители числа (исключая 1)
    factors = get_factors(num_elements)

    if not factors:
        print(f"Невозможно разбить число {num_elements} на множители без остатка.")
        return

    print(f"Возможные матрицы для числа {num_elements}:")
    for factor in factors:
        # Считаем размерности матрицы
        rows = factor
        cols = num_elements // factor
        matrix = np.random.random((rows, cols))  # Создаем случайную матрицу
        print(f"Матрица {rows}x{cols}:")
        print(matrix)


# Пример вызова функции с числом 12
generate_matrices(12)
