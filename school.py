from collections.abc import Iterable, Iterator


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


class StudentIteratorMatter1(Iterator):
    def __init__(self, students):
        self.__students = sorted(students,
                                  key=lambda s: s.get_note1(),
                                  reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter2(Iterator):
    def __init__(self, students):
        self.__students = sorted(students,
                                  key=lambda s: s.get_note2(),
                                  reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter3(Iterator):
    def __init__(self, students):
        self.__students = sorted(students,
                                  key=lambda s: s.get_note3(),
                                  reverse=True)
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students

    def __iter__(self):
        return StudentIteratorMatter1(self.__students)


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("\n--- Classement Matière 1 ---")
    for student in school_class:
        print(student)

    print("\n--- Classement Matière 2 ---")
    for student in StudentIteratorMatter2(school_class.get_students()):
        print(student)

    print("\n--- Classement Matière 3 ---")
    for student in StudentIteratorMatter3(school_class.get_students()):
        print(student)