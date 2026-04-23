a = int(input("Enter max value: "))

rows = a

for i in range (-1, rows + 1):
    for j in range(0, i):
        print(str(i), end= ' ')
