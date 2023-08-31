try:
    print(a)
except:
    print('переменная "a" не определена')

try:
    print(a)
except Exception as ex:
    print('переменная "a" не определена')
    print(ex)

try:
    k=1/0
    print(k)
except ZeroDivisionError:
    k=0
    print('app close')

#try:
    #k=1/0
    #print(k)
   # print(d)
#except ZeroDivisionError:
    #k=0
    #print('app close')

try:
    r=1/0
    #print(k)
except ZeroDivisionError:
    print('app close')
finally:
    print('finally')

x= -1
if x<0:
    raise Exception("Число меньше нуля")