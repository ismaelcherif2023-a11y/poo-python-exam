from collections.abc import Iterable, Iterator


def add_note4(cls):
    original_init = cls.__init__

    def new_init(self, name, note1, note2, note3, note4=0):
        original_init(self, name, note1, note2, note3)
        self._note4 = note4

    def get_note4(self):
        return self._note4

    cls.__init__ = new_init
    cls.get_note4 = get_note4
    return cls


@add_note4
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


def add_iterator_matter4(cls):
    class StudentIteratorMatter4(Iterator):
        def __init__(self, students):
            self.__students = sorted(students,
                                      key=lambda s: s.get_note4(),
                                      reverse=True)
            self.__index = 0

        def __next__(self):
            if self.__index >= len(self.__students):
                raise StopIteration
            student = self.__students[self.__index]
            self.__index += 1
            return student

    def iter_matter4(self):
        return StudentIteratorMatter4(self.get_students())

    cls.iter_matter4 = iter_matter4
    return cls


class SchoolClassSingleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


@add_iterator_matter4
class SchoolClass(Iterable, metaclass=SchoolClassSingleton):
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
    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 11))
    school_class.add_student(Student('V', 9, 14, 14, 18))

    print("\n--- Classement Matière 1 ---")
    for student in school_class:
        print(student)

    print("\n--- Classement Matière 2 ---")
    for student in StudentIteratorMatter2(school_class.get_students()):
        print(student)

    print("\n--- Classement Matière 3 ---")
    for student in StudentIteratorMatter3(school_class.get_students()):
        print(student)

    print("\n--- Classement Matière 4 ---")
    for student in school_class.iter_matter4():
        print(f'{student.get_name()} - Note4: {student.get_note4()}')

    # Test Singleton
    school_class2 = SchoolClass()
    assert school_class is school_class2
    print("\n✅ Singleton OK : même instance !")