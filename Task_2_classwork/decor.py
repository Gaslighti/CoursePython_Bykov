def currency(fn):
    def wrapper(*args,**kwargs):
        result=fn(*args,**kwargs)
        return f'{result} руб.'
    return wrapper


def price_calcilation(price,tax):
    return price*(1+tax)

price_calcilation=currency(price_calcilation)
print(price_calcilation(100,0.05))

@currency
def price_calcilation_2(price,tax):
    return price * (1 + tax)

print(price_calcilation_2(100,0.06))

# Напишите две функции:
# возвращает квадрат принимаемого числа
# возвращает произведение принимаемого числа и 2
# Напишите декоратор который добавляет к результату декорируемой функции строку “Результат вычислений: ”.
# Задекарируйте обе функции и выведите результат в консоль.

def print_result(f):
    def result(x):
        r= f(x)
        print(f'Результат вычислений: {r}')
        return r
    return result

@print_result
def square(x):
    return x**2

@print_result
def multiply(x):
    return x*2

square(3)
multiply(3)