username_OG = "python"
password_OG = "rules"

username = str(input("Enter username: "))
password = str(input("Enter password: "))
attempt = 1

while attempt < 5:
    if username == username_OG and password == password_OG:
        print("Welcome")
        break

    else:
        print("Incorrect username or password. Please try again.")

        attempt += 1

        username = str(input("Enter username: "))
        password = str(input("Enter password: "))
else:
    print("Access denied")
    