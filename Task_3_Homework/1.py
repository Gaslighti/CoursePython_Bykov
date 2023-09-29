# 1.	Создайте класс  прямоугольника. Класс принимает два параметра, ширина и высота прямоугольника.
# Создайте два метода:
# -	метод возвращающий площадь прямоугольника
# -	метод возвращающий периметр прямоугольника


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Создание объекта прямоугольника с шириной 5 и высотой 10
rect = Rectangle(5, 10)

# Получение площади и периметра
area = rect.area()
perimeter = rect.perimeter()

print(f'Площадь: {area}, Периметр: {perimeter}')
