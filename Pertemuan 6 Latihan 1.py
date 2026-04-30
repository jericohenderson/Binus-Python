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
