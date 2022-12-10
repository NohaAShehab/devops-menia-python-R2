
"""
    functions
"""
#
# def testfun():
#     print("Hello world")
#
# x= testfun()
# print(x)

# def printfullname(fname, lname):
#     fullname = f"{fname} {lname}"
#     print(fullname)
#     return fullname
#
# fullname = printfullname("Noha", "Shehab")
#
# printfullname("Ahmed", "Ali")

""" functions with default arguments """
# def printfullname(fname="", lname=""):
#     fullname = f"{fname} {lname}"
#     print(f"firstname = {fname}, lastname ={lname}")
#     print(f"fullname = {fullname}")
#     return fullname
#
# # printfullname()
# # printfullname("Ahmed")
# # printfullname("Ahmed", "Ali")
# printfullname(lname="Omar", fname="Ali")



""" python is loosly dynamically typed lang.? ----> interpreter detect datatype in the run """
# print(isinstance("noha" , str))
# def sumnums(num1 , num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1 = {num1}, num2= {num2}")
#         res = num1 + num2
#         print(res)
#     else:
#         print("please provide valid arguments ")
# sumnums(10 , 20)
# sumnums("Ahmed", "Ali")
#

# def sumnums(num1 , num2=9):
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1 = {num1}, num2= {num2}")
#         res = num1 + num2
#         print(res)
#     else:
#         print("please provide valid arguments ")
# sumnums(10 )


################################################
""" function with variable number of arguments """
# print("Ahmed", "Ali", True, "Hello world")

# def sumnums(*nums):  # function accept zero number of arguments or more argument
#     print(type(nums))
#     print(nums)
#
#
# sumnums()
# sumnums(2,4,5,56)
# sumnums(2)

#########################################

def introduceYourSelf(**kwargs):
    print(kwargs)

introduceYourSelf(name="Noha", work="iti", city="Cairo")
introduceYourSelf(fname="Ahmed")
introduceYourSelf()














