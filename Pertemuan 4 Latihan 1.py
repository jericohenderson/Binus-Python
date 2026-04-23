a = int(input("Enter max value: "))

rows = a

for i in range (rows, 0, -1):
    for j in range(0, i):
        print(str(i), end= ' ')
