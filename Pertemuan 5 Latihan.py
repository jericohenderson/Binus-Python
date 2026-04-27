def thisIsFunction():
    print("Jerico Henderson")
thisIsFunction()
def returnStringFunction():  
    return "Pondok Pinang Kuningan Kebayoran Lama"

x = returnStringFunction()

print(x)

print()

while True:
    
    menu = input("Enter Menu (+|-|/|*|%|stop): ").lower()

    
    if menu == 'stop':
        print("Program stopped. Thank you for using my program.")
        break

    
    try:
        val1 = float(input("Enter Value 1: "))
        val2 = float(input("Enter Value 2: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        continue

    
    if menu == '+':
        result = val1 + val2
        print(f"The result of addition {val1} + {val2} is {result}\n")
    
    elif menu == '-':
        result = val1 - val2
        print(f"The result of subtraction {val1} - {val2} is {result}\n")
    
    elif menu == '*':
        result = val1 * val2
        print(f"The result of multiplication {val1} * {val2} is {result}\n")
    
    elif menu == '/':
        if val2 != 0:
            result = val1 / val2
            print(f"The result of division {val1} / {val2} is {result}\n")
        else:
            print("Error: Division by zero is not allowed.\n")
            
    elif menu == '%':
        result = val1 % val2
        print(f"The result of modulo {val1} % {val2} is {result}\n")
    
    else:
        print("Invalid operator. Please try again.\n")
        
    
