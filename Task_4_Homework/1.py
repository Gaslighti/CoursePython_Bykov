# 1.	Создайте вектор размером 10 с рандомными значениями, отсортируйте и выведите в консоль.

import numpy as np

# Создаем вектор размером 10 с рандомными значениями
random_vector = np.random.random(10)

# Сортируем вектор
sorted_vector = np.sort(random_vector)

# Выводим отсортированный вектор в консоль
print("Отсортированный вектор:")
print(sorted_vector)
