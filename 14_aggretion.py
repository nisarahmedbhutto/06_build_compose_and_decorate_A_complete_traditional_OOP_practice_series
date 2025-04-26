class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: storing reference

    def show_details(self):
        print(f"Department: {self.department_name}")
        print(f"Employee: {self.employee.name} (ID: {self.employee.emp_id})")

# Creating Employee object independently
emp1 = Employee("Ali", 101)


dept1 = Department("HR", emp1)


dept1.show_details()
