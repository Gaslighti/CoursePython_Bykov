class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Stdent(Person):
    def __init__(self, course, first_name, last_name):
        self.course = course
        super().__init__(first_name, last_name)