print("1. USD to PKR")
print("2. PKR to USD")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    usd = float(input("Enter amount in USD: "))
    pkr = usd * 283.27
    print("Amount in PKR:", round(pkr, 2))

elif choice == 2:
    pkr = float(input("Enter amount in PKR: "))
    usd = pkr * 0.0035
    print("Amount in USD:", round(usd, 2))

else:
    print("Invalid choice!")
