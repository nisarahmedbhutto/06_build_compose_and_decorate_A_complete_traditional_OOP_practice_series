class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Creating object
m = Multiplier(5)

# Checking if object is callable
print(callable(m))  # Output: True

# Using object like a function
result = m(10)
print(result)  # Output: 50
