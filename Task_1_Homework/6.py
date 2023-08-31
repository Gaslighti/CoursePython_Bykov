#6)	Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.

a = [5,-10,15,29,-1]

def Positive_nambers(a):
    c=0
    for item in a:
        if item >0:
            c=c+1
    print(c)

Positive_nambers(a)