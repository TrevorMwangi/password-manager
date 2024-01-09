# master password
master_password = input("What is the master password?  ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name:  ")
    password = input("Password:  ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + password + "\n")
    

while True:
    mode = input("Would you like to add a password or view existing ones? (view/add)  Press Q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!!")
