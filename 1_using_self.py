
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"My Name Is: {self.name} ,And My Marks Is: {self.marks}")

student = Student("ali",88)
student.display()