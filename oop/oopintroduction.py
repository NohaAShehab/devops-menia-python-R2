""" general structure for the data
    define properties , functionalities

"""
# emp = {
#     "name":"ahmed",
#     "dept":"devops"
# }
#
# emp2 = {
#     "firstname":"ali",
#     "dept_name": "devops"
# }

"1- to define a class"


# class Employee:
#     pass
#
#
# e = Employee()
# print(e)
# e2= Employee()
# print(e2)

# class Employee:
#     def __init__(self):
#         print(f"------the object is being created ---> {self} ")
#         self.name= 'Ahmed'
#         self.email = "ahmed@gmail.com"
#
#
# e = Employee()
# print(e)
# e2= Employee()
# print(e2)

###################

# class Employee:
#     # ## __init__ special method used to construct the object.
#     def __init__(self, name, email):
#         # # self  ---> represents the object address in the memory
#         print(f"------the object is being created ---> {self} ")
#         ### instance variables ---> values depend on the instance
#         self.name = name
#         self.email = email
#
#
# e = Employee("Ahmed", "Ahmed@gmail.com")
# print(e.name)
# e2 = Employee("Ali", "ali@gmail.com")
# print(e2.email)
# e2.email = 'aliahmed@iti.com'
# print(e2.email)
# """ loosly dynamically typed lang. """
# e2.country = 'Cairo'
###############################
# class Employee:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     # instance method
#     def printEmp(self, message=''):
#         print(f"EmployeeInfo is {self.name}, {self.email}")
#         print(message)
#
#
# e = Employee("Ahmed", "Ahmed@gmail.com")
# e.printEmp("I love python")

########################################

# class Employee:
#     # class variables  ---->
#     nationality  = 'Egyption'
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     # instance method
#     def printEmp(self, message=''):
#         print(f"EmployeeInfo is {self.name}, {self.email}")
#         print(message)
#
#
# e = Employee("Ahmed", "Ahmed@gmail.com")
# e2 = Employee("Mohamed", "Mohamed@gmail.com")
# "access class variable"
# print(Employee.nationality)
# Employee.nationality= 'Morocooian'



# class Employee:
#     # class variables  ---->
#     nationality  = 'Egyption'
#     count = 0
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Employee.count +=1
#
#     # instance method
#     def printEmp(self, message=''):
#         print(f"EmployeeInfo is {self.name}, {self.email}")
#         print(message)
#
#     @classmethod
#     def countEmp(cls):
#         print(cls)
#         print(cls.count)
#
# e = Employee("Ahmed", "Ahmed@gmail.com")
# e2 = Employee("Mohamed", "Mohamed@gmail.com")
# "access class variable"
# print(Employee.nationality)
# Employee.nationality= 'Morocooian'
#
# Employee.countEmp()
##############################

class Employee:
    # class variables  ---->
    nationality  = 'Egyption'
    count = 0
    def __init__(self, name, email,salary):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count +=1


    # instance method
    def printEmp(self, message=''):
        print(f"EmployeeInfo is {self.name}, {self.email}")
        print(message)

    @classmethod
    def countEmp(cls):
        print(cls)
        print(cls.count)

    @staticmethod  # helper method
    def calnetsal(salary):
        return salary * .8

e = Employee("Ahmed", "Ahmed@gmail.com", 2000)
e2 = Employee("Mohamed", "Mohamed@gmail.com", 3000)
e2.printEmp()

print(Employee.calnetsal(e.salary))
print(Employee.calnetsal(100000))





