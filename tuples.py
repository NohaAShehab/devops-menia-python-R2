"""
tuple is immutable data type v--> o
nce created cannot be changed

"""
"1- to define a tuple "
t = ()
myt = tuple([])


"tuple can hold different values from different datatypes even if another list "
elements = ("Ahmed", True, 66, "Cairo", 3.14, ["python", 'django'],"Cairo", "Cairo")
"you can access tuple elements using the index "
print(elements[1])
print(elements[5][1])

"you can len of the tuple "
print(len(elements))
print(elements)

"tuple concatenation"
t1 = ("jenkins", "microservice")
t2 = ("docker", "Kubernetes", "jenkins")
courses = t1 + t2  # generate new list
print(courses)

"loop over the tuple"
for item in courses:
    print(item)

"membership"
print("docker" in courses)

"cast list to tuple?"
l  =["Ahmed", "Omar","iti", True, 2022]
myt = tuple(l)
print(myt)

myl = list(myt)
print(myl)

"cast string to list ?"
name = 'Ahmed'
name = tuple(name)
print(name)

"list or tuple ===> you can convert it string"
info = ["Omar", "iti", "Cairo"]
info = '_'.join(info)
print(info)

"tuple of one item"
tt = ("iti",)


