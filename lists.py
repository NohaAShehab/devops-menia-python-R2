"""
   list ---> most common datatype in python
   list is mutable datatype ---> you can change its content in the runtime

"""
"1- to define a list "
l  = []
myl = list([])
"list can hold different values from different datatypes even if another list "
elements = ["Ahmed", True, 66, "Cairo", 3.14, ["python", 'django'],"Cairo", "Cairo"]
"you can access list elements using the index "
print(elements[1])
print(elements[5][1])

"you can len of the list "
print(len(elements))
print(elements)

"update list "
elements[5] = 'devops'

"append element to the list "
elements.append("added element")

"insert element at certain position in the list "
elements.insert(3, "inserted value")

"pop element from the list "
# poppedelement = elements.pop()  #remove the last element from the list

poppedelement = elements.pop(2)  #remove the at index 2 from the list

"remove element from the list "
print(elements)
elements.remove("Cairo")
print(elements)

"list concatenation"
l1 = ["jenkins", "microservice"]
l2 = ["docker", "Kubernetes", "jenkins"]
courses = l1 + l2  # generate new list
print(courses)

"extend a list"
print(l1)
l1.extend(l2)  # list
print(l1)

"loop over the list"
# index  = 0
# for item in courses:
#     print(item)
#     if item=='jenkins':
#         courses.pop(index)
#         # courses.remove("jenkins")
#     index +=1
#
# print(courses)

""" sort list ===> list elements must be from the same type """

l = [3,4,1,400, 200, 1000, -1000]
# print(l)
# l.sort()
# print(l)

"###"
# print(l)
# l.sort(reverse=True)
# print(l)
"reverse a list---> any types"
mm = ["Ahmed", True, "python", 8 , "iti"]
mm.reverse()
print(mm)
"min , max"
print(min(l))

"membership"
print("Noha" in mm)


num = input("please enter number : ")
if num.isdigit():
    num = int(num)
    multiplication_table = []
    for i  in range(1,4):
        mulnum = []
        for j in range(1, i+1):
            mulnum.append(i*j)
        multiplication_table.append(mulnum)

    print(multiplication_table)
