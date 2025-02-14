class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("Jeffrey Digas", 23, "Information Technology")
student2 = Student("Arvy Buranday", 24, "Engineering")
student3 = Student("Jogie Lucion", 30, "Crimnology")

student1.introduce()
student2.introduce()
student3.introduce()
