""" any variable defined in the python script is considered to have global scope
    this variable can be accessed anywhere in the script
"""
# course = "python"
# def printHelloWorld():
#     print(f"from inside the function ---> {course}")
#
# printHelloWorld()
# print(f"From outside the function ====> {course}")
############################################

# course = "python"  # global scope
#
# def printHelloWorld():
#     course = "Django" # create new local variable in the scope
#     print(f"from inside the function ---> {course}")
# #
# printHelloWorld()
# print(f"From outside the function ====> {course}")


###############
""" modify the global variable from inside the function """

# course = "python"  # global scope
#
# def printHelloWorld():
#     global course
#     course = "Django" # create new local variable in the scope
#     print(f"from inside the function ---> {course}")
#
# print(f"From outside the function ====> {course}")
# printHelloWorld()
# print(f"after calling the function course ====> {course}")


"""
    global scope =---> variable with global can be accessed anywhere in the script
    
    localscope ---->   variables defined in the function can be accessed only from inside the function
        

"""

# def testfunction():
#     global name
#     name = 'Ahmed'  # local variable in the scope of the function ----> cannot be accesses anywhere
#     # outside the function.
#     print(f"from the function name = {name}")
#
# testfunction()
# print(name)

################
#
# def testfunction():
#     name = 'Ahmed'  # local variable in the scope of the function ----> cannot be accesses anywhere
#     # outside the function.
#     print(f"from the function name = {name}")
#
# testfunction()
# print(name)

###############################################
""" functions inside a function """

# def outerfun():
#     course = 'Python'  # local variable for the outerfun
#     def innerfunction():
#         print(f"Hello world ---> course = {course}")
#
#     innerfunction()
#
#
# outerfun()

#############################
# def outerfun():
#     course = 'Python'  # local variable for the outerfun
#     def innerfunction():
#         course = 'Kubernates'  # create new local variable for the innerfunction scope
#         print(f"Hello world ---> course = {course}")
#
#     innerfunction()
#     print(f"course after calling innerfunction= {course}")
#
#
# outerfun()

##############################
# def outerfun():
#     course = 'Python'  # local variable for the outerfun
#     def innerfunction():
#         nonlocal course
#         course = 'Kubernates'  # create new local variable for the innerfunction scope
#         print(f"Hello world ---> course = {course}")
#
#     innerfunction()
#     print(f"course after calling innerfunction= {course}")
#
#
# outerfun()
####################################

# def outerfun():
#     course = 'Python'  # local variable for the outerfun
#     def innerfunction():
#         nonlocal course
#         course = 'Kubernates'  # create new local variable for the innerfunction scope
#         print(f"Hello world ---> course = {course}")
#
#     innerfunction()
#     print(f"course after calling innerfunction= {course}")
#
#
# outerfun()
#############################

name = 'Ahmed'
def outerfun():
    course = 'Python'  # local variable for the outerfun
    def innerfunction():
        nonlocal course
        course = 'Kubernates'  # create new local variable for the innerfunction scope
        print(f"Hello world ---> course = {course}")
        global name
        name = 'Ali'

    innerfunction()
    print(f"course after calling innerfunction= {course}")


outerfun()
print(name)














































