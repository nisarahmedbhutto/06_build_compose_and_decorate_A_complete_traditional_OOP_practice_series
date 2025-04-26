
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def brak(self):
        print(f"{self.name} is barking....")


dog = Dog("buddy","labrador")
dog.brak()