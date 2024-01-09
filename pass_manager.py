# master password
password = input("What is the master password?  ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to add a password or view existing ones? (view/add)  Press Q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode!!")
