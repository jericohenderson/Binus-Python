class Student:
    def __init__(self):
       
        self._name = None
        self._score = None

   
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

  
    @name.setter
    def name(self, value):
        self._name = value

    @score.setter
    def score(self, value):
        self._score = value

    
    def delete_data(self):
        self._name = None
        self._score = None
        print("Data Successfully Deleted")

def main():
    student = Student()

    while True:
        print("\n===== OOP Program =====")
        print("1. Declare Object")
        print("2. Display Object")
        print("3. Change Object Value")
        print("4. Delete Object")
        print("5. Exit Program")
        
        choice = input("Enter Your Choice (1/2/3/4/5): ")

        if choice == '1':
            
            student.name = input("Enter Your Name: ")
            student.score = input("Enter Your Score: ")
            print("Data Successfully Added")

        elif choice == '2':
           
            print(f"\nName: {student.name}")
            print(f"Score: {student.score}")

        elif choice == '3':
            field = input("What would you like to change (Name/Score): ").strip().lower()
            if field == "name":
                student.name = input("Enter New Name: ")
                print("Name Data Successfully Changed")
            elif field == "score":
                student.score = input("Enter New Score: ")
                print("Score Data Successfully Changed")
            else:
                print("Invalid field.")

        elif choice == '4':
            student.delete_data()

        elif choice == '5':
            print("Program has ended. Thank you for using my program.")
            break
        
        else:
            print("Invalid choice. Please enter a value from 1 to 5")

if __name__ == "__main__":
    main()
