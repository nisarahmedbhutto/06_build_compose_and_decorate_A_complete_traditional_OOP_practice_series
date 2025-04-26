import random

class Random_numbers:

    @staticmethod
    def randint():
        return random.randint(1,10)
    
print(Random_numbers.randint())