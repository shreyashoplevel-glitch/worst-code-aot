def check_file():
    check_new_file = input("do you want to make a new file (y/n) ")
    if check_new_file.lower() == "y":
        return input("what is the name of your new file? ")