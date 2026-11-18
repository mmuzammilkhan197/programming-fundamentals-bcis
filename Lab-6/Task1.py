correct_username = "example123@gmail.com"
correct_password = "123456"

while True:
    username = input("Enter Username: ")

    if correct_username != username:
        print("Invalid Username!")
        continue

    password = input("Enter Password: ")

    if correct_password != password:
        print("Invalid Password!")
        continue

    print("Successfully Login......")
    break