# class Employee:
#     company_name =''
#     def __init__(self,ename,esalary,eid):
#         self.ename = ename
#         self.esalary =esalary
#         self.eid = eid 

#     def details(self):
#         print(f"Employee Name is {self.ename}\nAnd He/She is Getting Salary About: {self.esalary}\nAnd Employee ID: {self.eid}")


#     def salary_info(self):
#         if self.esalary >= 50000:
#             print(" Hello.. ",self.ename,"Congragulation You are getting more than 50k ")   
#         elif self.esalary <= 50000 or self.esalary >= 25000:
#             print("Hello ",self.ename, "Your Salary is :",self.esalary,"Work Samrt..") 
#         else:
#             print("Hello ",self.ename,"You aree getting low salary : ",self.esalary,"Work Hard .. ")
# employee1 =Employee('Shantesh',85000,2580)
# employee1.details()
# employee1.salary_info()

class Employee:
    company_name = 'XYZ Corp'
    
    def __init__(self, ename, esalary, eid):
        self.ename = ename
        self.esalary = esalary
        self.eid = eid 

    def details(self):
        print(f"\nEmployee Name: {self.ename}\nHe/She is Getting Salary About: {self.esalary}\nEmployee ID: {self.eid}\n")

    def salary_info(self):
        if self.esalary >= 50000:
            print(f"Hello {self.ename}, Congratulations! You are getting more than 50k.")
        elif 25000 <= self.esalary < 50000:
            print(f"Hello {self.ename}, Your Salary is {self.esalary}. Keep working smart!")
        else:
            print(f"Hello {self.ename}, You are getting a low salary of {self.esalary}. Work harder!")
            
# Take multiple employee inputs and store them in a list
def get_employee_data():
    employees = []
    
    num_employees = int(input("Enter the number of employees: "))
    
    for i in range(num_employees):
        print(f"\nEnter details for Employee {i+1}:")
        ename = input("Enter Employee Name: ")
        esalary = int(input("Enter Employee Salary: "))
        eid = int(input("Enter Employee ID: "))
        
        # Create Employee object and add to list
        employee = Employee(ename, esalary, eid)
        employees.append(employee)
    
    return employees

# Iterating through the list of employees and printing their details
employees = get_employee_data()

for emp in employees:
    emp.details()
    emp.salary_info()
