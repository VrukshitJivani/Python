try:
    username = input("Username: ")
    password = input("Password: ")

    if username != "admin" or password != "1234":
        raise PermissionError("Invalid login")

    print("Login successful")

except PermissionError as e:
    print("Login failed:", e)