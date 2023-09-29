# 2.	Напишите программу - виртуальную модель процесса обучения.

class Materials:
    def __init__(self, *args):
        self.materials_list = list(args)


class Student:
    def __init__(self):
        self.knowledge = []

    def take(self, material):
        self.knowledge.append(material)


class Teacher:
    def __init__(self):
        self.taught_students_count = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
            self.taught_students_count += 1


# Создание объекта учебных материалов
materials = Materials(
    "Python",
    "Version Control Systems",
    "Relational Databases",
    "NoSQL databases",
    "Message Brokers"
)

# Создание объекта учителя
teacher = Teacher()

# Создание объектов учеников
students = [Student() for _ in range(4)]

# Проведение занятий по каждому материалу
for material in materials.materials_list:
    teacher.teach(material, *students)

# Вывод знаний каждого ученика
for i, student in enumerate(students, 1):
    print(f'Ученик {i}: {student.knowledge}')
