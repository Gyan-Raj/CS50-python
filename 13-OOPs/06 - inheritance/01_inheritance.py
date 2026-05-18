class Human:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name


class Student(Human):
    def __init__(self, name, std):
        super().__init__(name)
        self.standard = std


class Teacher(Human):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


human = Human("Gyan")
student = Student("Gyan", "12th")
teacher = Teacher("Gyan", "English")

print("human: ", human.name)
print("student", student.name, student.standard)
print("teacher", teacher.name, teacher.subject)
