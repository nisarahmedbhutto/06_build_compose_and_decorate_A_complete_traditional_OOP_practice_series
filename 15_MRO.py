class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):  # Diamond inheritance
    pass

# Create object of D
d = D()
d.show()

# Let's also print the MRO
print(D.__mro__)
