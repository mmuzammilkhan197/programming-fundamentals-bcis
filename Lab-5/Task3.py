line = int(input("Enter the number of line: "))
for i in range(1 ,line + 1):
    for j in range(i):
        print("*",end=" ")
    print()

print(f"The number of line is: {line}")