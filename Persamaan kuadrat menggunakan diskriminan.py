#Input
nilai a
nilai b
nilai c

if a == 0:
  print ("bukan persamaan kuadrat")

else:
  dis = b**2 - 4*a*c

   if dis > 0:
     root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
        print(f"Two distinct real roots: {root1} and {root2}")
   elif dis == 0:
        
        root = -b / (2 * a)
        print(f"One repeated real root: {root}")
    
    else:
        
        root1 = (-b + cmath.sqrt(dis)) / (2 * a)
        root2 = (-b - cmath.sqrt(dis)) / (2 * a)
        print(f"Two complex roots: {root1} and {root2}")
 


