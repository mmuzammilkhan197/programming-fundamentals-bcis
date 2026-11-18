principal_amount = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

si = (principal_amount * rate * time) / 100

print("Simple Interest:", round(si, 2))