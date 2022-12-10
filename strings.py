# work = "Information Technology Institute"
#
# print(work[2:8]) # get string from start to end-1
#
# print(work.count("o"))
#
# print(work[-1])
#
# print(work[0])

################
"1- string concat  between string only  "
fname ="Noha"
midname = 'AbdelHady'
lname ='Shehab'

# fullname = fname + midname + midname + lname


# print(fullname)
"2- string interpolation"
# fullname = fname + midname*2 + lname
# print(fullname)
#
# print(fullname + 10)

"3- string replace "
greet = 'Hi @, Nice to meet @ @ @ '
print(greet.replace("@", "Ahmed"))

# name = 'Ahmed' ; email = "Ali"

# mystring = 'Ahmed10'
# print(mystring.isdigit())
# print(mystring.isalpha())

# mystring = '                '
# print(mystring.isspace())
# name = 'noha'
# print(name.upper())
# print(name.lower())

"stripping the string"
# message = "         My name is Noha                   "
#
# print(len(message))
# print(message)
# # message = message.strip()  # strip spaces from the beginning and the end of the string
# # print(message)
# # message = message.lstrip()  # strip spaces from the beginning
# # print(message)
# message = message.rstrip()  # strip spaces from the beginning
# print(message)

#
# mystring = "##           . Hello, # I love python .      ##"
# # mystring = mystring.strip("# ")
# # print(mystring)
#
# # mystring = mystring.rstrip("# ")
# # print(mystring)
# mystring = mystring.lstrip("# ")
# print(mystring)
""" string formating """
# temp = "My name is {0}, I lives at {1}"
# print(temp.format("Noha", "Cairo"))
# print(temp.format("Ahmed", "Alex"))
# print(temp.format( "Assuit", "Ali"))

temp = "My name is {username}, I lives at {usercity}"
# print(temp.format("Noha", "Cairo"))
print(temp.format(username="Ahmed",usercity="Alex"))
# print(temp.format( usercity="Assuit", username="Ali"))
# print(temp.format( "Assuit", "Ali"))

"f- format string "
# name = 'omar'
# name = 'Noha'
# city = 'Cairo'
# temp = f"My names is {name}, I lives in {city}"
# print(temp)


# name = input("please enter your name : ")# return with string
# city = input("please eneter your city: ")
# if name =='noha':
#     print("hi")
# else:
#     print("bye")
# temp =f"My name is {name} , I lives in {city}"
#
# print(temp)


# age = input("please enter age : ")
# if age.isdigit():
#     age = int(age)


# print(min(10, 11, round(3.3)))
#
#
# ####
# c = 4 + 5j  # imaginary part
#
# print(c)

###############################