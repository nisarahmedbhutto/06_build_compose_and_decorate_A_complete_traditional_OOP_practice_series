from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init_(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

rect = Rectangle(5,3)
print(rect.area())