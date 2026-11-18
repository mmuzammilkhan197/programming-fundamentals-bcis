correct_password = "123456"

for attempt in range(1, 4):
    password = input("Enter Password: ")

    if password == correct_password:
        print("Successfully Login!")
        break
    else:
        print("Incorrect Password!")

else:
    print("Account Locked")
