# 1.	Создайте DataFrame с рандомными целыми числами от 1 до 10, размером 10х10

import pandas as pd
import numpy as np
import random

# Устанавливаем seed для воспроизводимости результатов
random.seed(42)

# Генерируем DataFrame с рандомными целыми числами от 1 до 10 размером 10x10
data = np.random.randint(1, 11, size=(10, 10))
df = pd.DataFrame(data, columns=[f'col{i+1}' for i in range(10)])

# Выводим DataFrame
print(df)
