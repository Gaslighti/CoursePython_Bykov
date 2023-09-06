def main(a,b):
    return a+b


# вызываем функцию
main(1,2)

print(main(23,89))

result_main=main(23,89)

def arg(a,b,c=2,d=3):
    return a+b+c+d


print(arg(1,1,1,1))

print(arg(1,1))

def range_arg(a,b,c,d):
    return a+''+b+''+c+''+d


print(range_arg('1','2','3','4'))

print(range_arg('1','2',d='3',c='4'))

# Напишите функцию принимающую 1 аргумент — сторону квадрата, и
# возвращающую 2 значения (с помощью кортежа): периметр квадрата, площадь квадрата


#def function(*args):


def add(*args):
    value=0

    for item in args:
        if isinstance(item,(int,float)):
            value += item

    return value


total = add(1,'dunctions',2,3,4,'Python',5.0,'kwargs')
print('Total:', total)


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kone='one', ktwo=2,kthree=3.0)
