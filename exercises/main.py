from module_password import generate_password

def run():
    length = int(input("Enter the long of your password: "))
    password = generate_password(length)
    print ('Password generated is: ' + password)


if __name__ == "__main__":
    run()