ticket_price = 500
age = int(input("Enter your age: "))

if age < 12:
    ticket_price = ticket_price * 0.5
    print("Ticket price:", ticket_price)

elif age >= 60:
    ticket_price = ticket_price * 0.7
    print("Ticket price:", ticket_price)

else:
    print("Ticket price:", ticket_price)
