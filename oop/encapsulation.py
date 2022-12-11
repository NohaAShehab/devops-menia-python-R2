"""
    Access modifiers
    public
    private ---> can be accessed only in the class  ---> __variable
    protected --> can be accessed only in the class or the derived class ---> _variable

"""


# class Employee:
#
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email
#         self.__salary = salary
#
#     def printEmp(self):
#         print(f"{self.name}, {self._email}, {self.__salary}")
#
# e = Employee("Ahmed", "ahmed@gmail.com", 2000)
# e.printEmp()
# # print(e.__salary)
# print(e._email)  #please don't do this
# e._email = 'mm@email.com'
# e2 = Employee("Ahmed", "ahmed@gmail.com", "iti")
################################
""" setter and getter """

# class Employee:
#
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email
#         self.__salary = salary
#
#
#     def getSalary(self):
#         return self.__salary
#
#
#     def setSalary(self, salary):
#         self.__salary = salary
#
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 2000)
# e.printEmp()
####################
class Employee:

    def __init__(self, name, email, salary):
        self.name = name  # public
        self._email = email
        self.salary = salary

    @property
    def salary(self):
        return self.__salary*.8

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            self.__salary = salary
        else:
            self.__salary = 0


# e = Employee("Ahmed", "ahmed@gmail.com", 2000)
# print(e.salary)
# # e.setSalary(30000)
# e.salary= "iti"
# e.name= 'ahmed@gmail.com'

e2 = Employee("Ahmed", "ahmed@gmail.com", "iti")
print(e2.salary)
# e.setSalary(30000)








