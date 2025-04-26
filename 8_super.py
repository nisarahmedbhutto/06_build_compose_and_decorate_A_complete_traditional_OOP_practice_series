class Student:

    def __init__(self,name,age,clas,):
        self.name = name
        self.age = age
        self.clas = clas

    def activity_to_class(self):
        return f"my name is {self.name} and my age is {self.age} i am student of {self.clas}"
    
class Teacher(Student):
    def __init__(self,name,age,clas,qualification):
        super().__init__(name,age,clas)
        self.qualification = qualification

        
    def teacher_intro(self):
        return f"i am {self.name} and my qualification is {self.qualification}"
    

student = Student("nisar",25,'10th')
print(student)
print(student.activity_to_class())


teacher = Teacher("ali",33,"math",'BA')
print(teacher)
print(teacher.teacher_intro())