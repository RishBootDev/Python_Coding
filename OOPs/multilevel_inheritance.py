class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"The name of the student is {self.name}")

class Graduate(Student):

    def __init__(self, name, graduation_year):
        super().__init__(name)
        self.graduation_year = graduation_year

    def display(self):
        print(f"The student is an undergraduate student with graduation year : {self.graduation_year} and the name: {self.name}")

class PostGraduate(Graduate):

    def __init__(self, name, graduation_year, thesis):
        super().__init__(name, graduation_year)
        self.thesis = thesis

    def display(self):
        print(f"Postgraduate student with {self.name} and thesis : {self.thesis}")


ob = PostGraduate("Aman", 2026, "Physics")

print(ob.display())