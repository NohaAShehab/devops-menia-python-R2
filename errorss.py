"""---------------------- Exception handling ----------------"""
""" logical errors"""

# def sumnum(num1, num2):
#     res = num1 * num2
#
#     print(res)
#
# sumnum(3,2)

""" runtime errors ---> Exceptions ----> You must handle it ? """

# print("------ Good morning ---------------")
#
# print(name)
print("----------------------------")
# try:
#     print(name)
# except:
#     print("cannot print name ")
#
# print("----------------- > end <------------------")
#############################
# try:
#     print(name)
# except Exception as myexception :
#     print(f"error happended ---> {myexception}")
#
# print("----------------- > end <------------------")


# try:
#     print(9/0)
# except Exception as myexception :
#     print(f"error happended ---> {myexception}")
#
# print("----------------- > end <------------------")

# num = input("please enter num ")
# try:
#     num = int(num)
# except Exception as myexception :
#     print(f"error happended ---> {myexception}")
#
# print("----------------- > end <------------------")


# num = input("please enter num ")
# try:
#     num = int(num)
# except Exception as myexception :
#     print(f"error happended ---> {myexception}")
# else:
#     num +=5
#     print(num)
#
# print("----------------- > end <------------------")


# def askfornum():
#     while True:
#         num= input("please enter number ")
#         if num.isdigit():
#             return num
#
#
# askfornum()
#
#############################

# num = input("please enter num ")
# try:
#     num = int(num)
# except Exception as myexception :
#     print(f"error happended ---> {myexception}")
# else:
#     num +=5
#     print(num)
# finally:
#     print("----> this block will be executed if problem happened or not .... ")
#     print("--------------- Process completed --------------------")
# print("----------------- > end <------------------")

""" -------------- Raising the exception ---------------------- """
# def askfornum():
#     while True:
#         num= input("please enter number ")
#         if num.isdigit():
#             return int(num)
#
#
# def calculator():
#     num1= askfornum()
#     num2 = askfornum()
#
#     operation = input("please enter operation : ")
#     if operation=='/':
#         if num2 == 0:
#             raise Exception("division by Zero is not allowed")
#         print("------- division operation is being processes ")
#         print("-==========================")
#         num1 = num1*10
#         print(num1)
#         res  = num1/ num2
#         print(res)
#
# calculator()
#
# print("==========================")
#





















