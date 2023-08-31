#	напишите функцию которая
#a)	принимает два списка
#b)	возвращает длину самого длинного

a = [5,10,15,29] #списки
b = [5,10,15,29,25] #списки

def Mlength_string(spis1,spis2): #Функция
    spis1=(len(a))
    spis2=(len(b))

    if spis1<spis2:
        print(spis2)
    else:
        print(spis1)

Mlength_string(a,b)
