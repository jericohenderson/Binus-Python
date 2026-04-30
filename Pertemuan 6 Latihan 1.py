class Employee:
    "Common base class for all employees"
    empCount = 0
    
    def __init__(self, name="Employee", salary=5000):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employees: %d" % Employee.empCount)
    
    def printEmployee(self):
        print("Name:", self.name, "\nSalary:", self.salary)

employee1 = Employee("Jerico", 5000)

employee1.printEmployee()
employee1.displayCount()
