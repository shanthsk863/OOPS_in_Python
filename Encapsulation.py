class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private variable

    def get_salary(self):
        return self.__salary  # Public method to access the private variable

emp = Employee("John", 50000)
print(emp.name)  # Accessible
print(emp.get_salary())  # Accessing private variable via public method
