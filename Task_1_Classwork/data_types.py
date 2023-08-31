age =25
print("Возраст", age)

count = 15
print("Количество", count)

'''Операции над числами'''
print(6+2)
print(6-2)
print(6*2)
print(6/2)

print(7//2) #Получение целого числа
print(7%2) #Получение остатка

print(6**2) #степень

'''СТРОКИ'''

s = 'ЭТО СТРОКА'
print(s +'\n')

g = '''Многострочная
    строка'''
print(g+'\n')

'''Операции над строками'''
print("Сложение"+"строк")
print("Умножение"*3)
print(len("тест")) #получение длины строки

#подстроки

a = 'auto'
print(a[0])
print(a[-1])
print(a[0:2])
print(a.index('t')) #индекс элемента

'''Списки'''

a = [5,10,15,29,25,30,35,40]
b=['str',1,[0,1,2],1.5]
test_list = ['один','два','three','four','five']

'''Операции над списками'''

print('a[2]= ', a[2])
print('a[0:3]= ', a[0:3])

#change element
a[2]=4
print(a)

for elem in test_list: #cicle for list
    print(elem)

print(len(test_list)) #get length list

test_list.append('six') #add value in list

print(test_list)

'''Логический тип'''

print(10>9)
print(10==9)
print(10<9)

a= True
if a:
    print('a = True')
else:
    print('a != True')



