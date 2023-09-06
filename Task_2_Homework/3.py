# 3.	Напишите функцию, которая принимает любое количество не
# именованных аргументов и возвращает кортеж состоящий из аргументов у которых тип данных str

def filter_strings(*args):
    return tuple(filter(lambda x: isinstance(x, str), args))

result = filter_strings(11, "Kiss", 5.5, "AC/DC", [1,'Nirvana'], "Metallica")
print(result)