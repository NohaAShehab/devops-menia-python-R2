# """
#     loosely dynamically typed lang.
#
#
# """
# num = 10
# name = 'Ahmed'
# Name = 'Ali'
# paragraph = "My name is " \
#             "Noha"
#
# print(paragraph)
#
# "multi-line string "
#
# myparagraph = """My name
# is Noha
# """
# print(myparagraph)
#
# # this a comment
#
# """ this acts like a comment """
# "this acts like a comment "
#
# name= False
### type casting
# "1- cast int to string"
# num = 20
# print(type(num))
#
# num = str(num)

######
"2- cast string to int "
# num = '300'
# num = int(num)

message = '10'
# message = int(message)
print(message.isdigit())
# if message.isdigit():
#     message = int(message)
#     print(message)
# else:
#     print("cannot cast string to int ")
"""
    if(message.isdigit()){
    print("hi")
    }
"""
# if message.isdigit():
#     print("hiii")
###############################################################3
# fullname = 'Noha Shehab'
#
# grade = 10000
#
# l = ["Ahmed", True, "Noha Shehab", 1000]
################### operators
num = 10
# num = num + 5


num +=5

###########3
# True == 1
# False == 0

###########################
"""
    values 
    Truly values ---> values in boolean context means True 
    
    falsy values  ---> values in boolean context means False 
    False , 0 , "", '', """""" , ''''''
"""

print(2 and 100)

print('noha' and "Samar" and "iti")

print('noha' and "" and "iti")



print('noha' or "Samar" or "iti")











