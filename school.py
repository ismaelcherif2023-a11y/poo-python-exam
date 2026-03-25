class Student:
    def __init__(self, name, note1, note2, note3):
        self.__name = name
        self.__note1 = note1
        self.__note2 = note2
        self.__note3 = note3

    def get_name(self):
        return self.__name

    def get_note1(self):
        return self.__note1

    def get_note2(self):
        return self.__note2

    def get_note3(self):
        return self.__note3

    def get_average(self):
        return (self.__note1 + self.__note2 + self.__note3) / 3

    def __str__(self):
        return (f'{self.__name} - '
                f'Notes: {self.__note1}, {self.__note2}, {self.__note3} - '
                f'Moyenne: {self.get_average():.2f}')


class SchoolClass:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students