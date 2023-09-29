# 3.	Напишите программу - доработанная виртуальную модель процесса обучения.

import random

# Список известных имен для учеников
known_names = ["Алиса Петрушкина", "Иван Голубков", "Алексндр Дуремар", "Денис Раков"]


class Human:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f'ФИО: {self.full_name}, Возраст: {self.age}, Пол: {self.gender}'


class Materials:
    def __init__(self, *args):
        self.materials_list = list(args)

    def __len__(self):
        return len(self.materials_list)


class Student(Human):
    def __init__(self, full_name, age, gender, student_number):
        super().__init__(full_name, age, gender)
        self.knowledge = set()
        self.student_number = student_number

    def take(self, material):
        self.knowledge.add(material)

    def __len__(self):
        return len(self.knowledge)

    def forget(self):
        num_to_forget = len(self.knowledge) // 2
        for _ in range(num_to_forget):
            if self.knowledge:
                self.knowledge.remove(random.choice(list(self.knowledge)))

    def get_info(self):
        return f'Студент {self.student_number}: {super().get_info()}, Знания: {self.knowledge}'


class Teacher(Human):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.taught_students_count = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)

        # Проверяем, прошли ли все материалы
        all_materials = set(materials.materials_list)
        for student in students:
            if student.knowledge == all_materials:
                self.taught_students_count += 1

    def get_info(self):
        return super().get_info() + f', Количество обученных учеников: {self.taught_students_count}'


# Создание объекта учебных материалов
materials = Materials(
    "Python",
    "Version Control Systems",
    "Relational Databases",
    "NoSQL databases",
    "Message Brokers"
)

# Создание объекта учителя
teacher = Teacher("Mr. Smith", 35, "Male")

# Создание объектов учеников с индивидуальными именами
students = [Student(name, 20 + i, 'Male', i + 1) for i, name in enumerate(random.sample(known_names, len(known_names)))]

# Проведение занятий по каждому материалу
for material in materials.materials_list:
    teacher.teach(material, *students)

# Ученики случайно забывают часть своих знаний
for student in students:
    student.forget()

# Вывод информации о каждом ученике
for student in students:
    print(student.get_info())

# Вывод информации о учителе
print(f'Учитель: {teacher.get_info()}')








