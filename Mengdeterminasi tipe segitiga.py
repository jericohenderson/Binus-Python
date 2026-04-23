a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))
c = float(input("Enter Side C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
  if a == b == c:
      print("Equilateral")
  elif a == b or b == c or c == a:
      print("isosceles")
  else:
      print("scalene")

else:
    print("not a triangle")
