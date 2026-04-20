# Menghitung diskriminan
calculate_discriminant()
print("Persamaan kuadrat: ax^2 + bx + c = 0")
#input
a = float(input('Enter coefficient a: '))
b = float(input('Enter coefficient b: '))
c = float(input('Enter coefficient c: '))

# Menghitung diskriminasi
    discriminasi = (b**2) - (4*a*c)
    
    print(f"\nDiscriminant value: {discriminant}")
    
    
    if discriminant > 0:
        print('Two distinct real solutions.')
    elif discriminant == 0:
        print('One real solution (equal roots).')
    else:
        print('No real solutions (complex roots).')

# Print function
calculate_discriminant()
