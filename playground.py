
"import module in another module "
""" 1- import all module """
# import inputsmodule  # here I can access the askforint, askforstring
#
# # myname = askforstring("Please enter firstname: ")
# def askforfullname():
#     fname = inputsmodule.askforstring("please enter firstname: ")
#     lname = inputsmodule.askforstring("please enter lastname: ")
#     print(f"{fname} {lname}")
#
#
# askforfullname()


# """ Alias the module name """
#
# import inputsmodule  as im # here I can access the askforint, askforstring
#
# # myname = askforstring("Please enter firstname: ")
# def askforfullname():
#     fname = im.askforstring("please enter firstname: ")
#     lname = im.askforstring("please enter lastname: ")
#     print(f"{fname} {lname}")
#
#
# askforfullname()
""" 2- import part of the module """
#
# from inputsmodule import  askforstring
# def askforfullname():
#     fname = askforstring("please enter firstname: ")
#     lname = askforstring("please enter lastname: ")
#     print(f"{fname} {lname}")
#
#
# askforfullname()


"3-import module from a package "
# import devopspkg.greeting
#
# devopspkg.greeting.sayWelcome("Ahmed", "Nice to meet you")

# import devopspkg.greeting as greet
#
# greet.sayWelcome("Ahmed", "Nice to meet you")
##################################################

"4- import part of module from a package "
# from devopspkg.greeting import sayHelloworld
#
# sayHelloworld("Ali")
################################################

# import  iti.helloModule
#
# iti.helloModule.helloWorld("Ahmed")

# from iti.helloModule import  helloWorld
# helloWorld("Ali")

from iti import HelloFriend

HelloFriend("Ali", "good morning")


l = [3,4,5,6]