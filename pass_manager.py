from cryptography.fernet import Fernet

# master password here
master_password = input("What is the master password?  ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: ", user, "| Password: ", passw)

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + password + "\n")
    

while True:
    mode = input("Would you like to add a password or view existing ones? (view/add) Press Q to quit   ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!!")
