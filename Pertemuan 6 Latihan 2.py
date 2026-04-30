class Student:
    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score

    def declare_data(self, name, score):
        self.name = name
        self.score = score
        print("Data Successfully Added")

    def display_data(self):
        print(f"\nName: {self.name}")
        print(f"Score: {self.score}")

    def change_data(self, field, new_value):
        if field.lower() == "name":
            self.name = new_value
            print("Name Data Successfully Changed")
        elif field.lower() == "score":
            self.score = new_value
            print("Score Data Successfully Changed")
        else:
            print("Invalid field selected.")

    def delete_data(self):
        self.name = None
        self.score = None
        print("Data Successfully Deleted")

def main():
   
    student_obj = Student()

    while True:
        print("\n===== OOP Program =====")
        print("1. Declare Object")
        print("2. Display Object")
        print("3. Change Object Value")
        print("4. Delete Object")
        print("5. Exit Program")
        
        choice = input("Enter Your Choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter Your Name: ")
            score = input("Enter Your Score: ")
            student_obj.declare_data(name, score)

        elif choice == '2':
            student_obj.display_data()

        elif choice == '3':
            field = input("What would you like to change (Name/Score): ")
            new_val = input(f"Enter New {field.capitalize()}: ")
            student_obj.change_data(field, new_val)

        elif choice == '4':
            student_obj.delete_data()

        elif choice == '5':
            print("Program has ended. Thank you for using my program.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
