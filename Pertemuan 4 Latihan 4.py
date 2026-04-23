while True:

    side_a = float(input("Enter Side A: "))
    side_b = float(input("Enter Side B: "))
    side_c = float(input("Enter Side C: "))
    
    
    if side_a == side_b == side_c:
        print("It is an Equilateral Triangle")
    
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        print("It is an Isosceles Triangle")
    
    else:
        print("It is a Scalene Triangle")
        
    
    repeat = input("\nDo you want to repeat? ").upper()
    if repeat != "Y":
        print("Program Stops")
        break
    print()
