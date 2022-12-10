

def askforstring(message):
    while True:
        mystring = input(message)
        if mystring.isalpha():
            return mystring

        print(f"Error! ======> please {message} again")



def askforInt(message):
    while True:
        myint = input(message)
        if myint.isdigit():
            return int(myint)

        print(f"Error! ======> please {message} again")


# age = askforInt("please enter your age ")
# print("--------------------------------")