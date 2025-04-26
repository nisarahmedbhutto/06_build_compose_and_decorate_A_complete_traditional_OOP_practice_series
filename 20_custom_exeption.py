# Step 1: Create custom exception
class InvalidAgeError(Exception):
    pass

# Step 2: Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18!")
    else:
        print("Age is valid.")

# Step 3: Handle with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
except ValueError:
    print("Please enter a valid integer age!")
