print(dir(object))

help(object.__new__)


class Student:

    students = []
    limit = 3

    def __new__(cls, *args, **kwargs):
        if len(cls.students) >= cls.limit:
            raise RuntimeError(f"Instance limit reached: {cls.limit}")
        insance = object.__new__(cls)
        cls.students.append(insance)
        return insance


s1 = Student()
s2 = Student()
s3 = Student()

print(Student.__dict__)

s4 = Student()
