"""
    dict ---> key value pair datatype
    dict ---> doesn't key duplication
"""
info = ["Noha","Engineering", "iti"]

info = {
    "name":"Noha",
    "faculty":"Engineering",
    "work":["iti" ,"IBM"]

}

"to define a dict "
d = {}
myd = dict([])

"access elements using key"
print(info["faculty"])
info["name"]="Noha Shehab"
info["age"] = 30

"get len of dict"
print(len(info))

"get keys of the dict"
keys = info.keys()
keys = list(keys)
print(keys[0])
##

"get values of the dict"
values = info.values()
print(values)
values = list(values)
print(values[0])


"get items of the dict"
items = info.items()
print(items)
items = list(items)

"loop over the dict "
for item in info:
    print(f"item  = {item}, {info[item]}")

for k,v in info.items():
    print(f"{k}, {v}")

"check membership "
print("name" in info)  # check in the keys
print("Noha Shehab" in info.values())  # check in the keys

"update a dict "
external_data = {
    "name": ["Ahmed", "Noha"],
    "courses" : ["python", "Admin01", "test"],
    'branches': ["Smart", "Menia","Alex", "Mansoura"]
}

info.update(external_data)
print(info)

"clear , del"

# info.clear()
#
# del info  # remove variable from the memory
print(info)
del info["name"]
print(info)


"pop value from the dict"

popped=info.pop("work")
print(popped)



for i in range(10):
    if i==4:
        continue
    print(i)
else:
    print("------------- loop reached the end ---------------")


for i in range(5):
    pass

print("-----------------")