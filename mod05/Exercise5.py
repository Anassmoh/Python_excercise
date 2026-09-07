login_username = "python"
login_password = "rules"
attempt = 0
while attempt < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    attempt += 1
    if username == login_username and password == login_password:
        print("Welcome")
        break
    elif attempt < 5:
        print("Incorrect username or password. Please try again.")
    # elif needed in order to really check the last attempt before locking up.
else:
    print("Access denied")