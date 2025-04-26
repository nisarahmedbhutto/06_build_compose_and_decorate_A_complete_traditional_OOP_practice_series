
class Employe:
    def __init__(self):
        self.name = "nisar"
        self._salary = 50000
        
        self.__ssn = '123-456-789'
    
emp = Employe()
print(emp.name)
print(emp._salary)



