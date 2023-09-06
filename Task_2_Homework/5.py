# 5.	Лесенка.
# Лесенкой - условный набор кубиков, в котором каждый последующий слой содержит меньше кубиков, чем предыдущий.
#
# Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков.
# -	Длина каждой ступени может отличаться.
# -	n - натуральное число в диапазоне от 1 до 100.

x=11 # Количество кубиков
def Ladder(n):
    def helper(remaining, prev_height):
        if remaining == 0:
            return 1
        if prev_height == 1:
            return 0

        ways = 0
        for next_height in range(1, min(prev_height, remaining + 1)): # цикл проверки кубиков
            ways += helper(remaining - next_height, next_height)

        return ways

    return helper(n, n)


print(Ladder(x)) # Количество возможных вариантов лестниц из этого количества кубиков