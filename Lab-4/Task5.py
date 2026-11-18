sales = float(input("Enter sales amount: "))

if sales < 1000:
    commission = sales * 5 / 100

elif sales <= 5000:
    commission = sales * 10 / 100

else:
    commission = sales * 15 / 100

print("Sales Amount:", sales)
print("Commission:", commission)
