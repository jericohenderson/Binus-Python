class Student:
    "Common base class for all students"
    stuCount = 0
    
    def __init__(self, name="Employee", salary=5000):
        self.name = name
        self.score = score
        Student.stuCount += 1
        
    def displayCount(self):
        print("Total Students: %d" % Students.stuCount)
    
    def printStudent(self):
        print("Name:", self.name, "\nScore:", self.score)
    
    
    def getScore(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "Salary":
            return self.salary
        else:
            return "Data Not Found"
    
    
    def setStudemt(self, name, salary):
        self.name = name
        self.salary = salary

student1 = Student()

student1.printStudent()
employee1.displayCount()


StudentName = student1.getStudent("Name")
print("The student's name is", studentName)


Student1.setStudent("Jericor", 90)
employee1.printEmployee()
