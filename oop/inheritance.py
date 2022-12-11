
# class Human:
#     def __init__(self, name, bdate):
#         self.name = name
#         self.bdate = bdate
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Employee(Human):
#    pass
#
#
# e = Employee("aHMED", 1990)
# e.speak()
################################################

# class Human:
#     def __init__(self, name, bdate):
#         self.name = name
#         self.bdate = bdate
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Employee(Human):
#    def __init__(self, name, bdate, salary):
#        super().__init__(name, bdate)
#        self.salary= salary
#
#    def work(self):
#        print(f"this employeee works with {self.salary} permonth")
#
# e = Employee("aHMED", 1990, 10000)
# e.speak()
# e.work()


########## single inheritance , multiple inheritance


class Human:
    def __init__(self, name, bdate):
        self.name = name
        self.bdate = bdate

    def speak(self):
        print(f"My name is {self.name}")


class Employee(Human):
   def __init__(self, name, bdate, salary):
       super().__init__(name, bdate)
       self.salary = salary

   def work(self, dept = None, location='cairo'):
       print(f"this employeee works with {self.salary} permonth {dept} {location}")

   def speak(self):
       super().speak()
       print(f"My salary is {self.salary}")

e = Employee("aHMED", 1990, 10000)
e.speak()
e.work(dept='devops')
e.work()
e.work('devops', "menia")

