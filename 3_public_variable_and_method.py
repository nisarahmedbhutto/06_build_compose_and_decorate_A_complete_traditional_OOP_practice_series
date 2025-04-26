
class Car:

    def __int__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting....")



car = Car("Honda")
print(car.brand)
car.start()