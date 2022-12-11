""" simple text files """

"""

    openfile ----> opening mode (read , write, append) ---> r ---> read, w---> write , a --> append 
    read / write 
    close file 
"""
"""1------- read data from file ------------"""
try:
    fileobj = open("info/info.txt", "r") #fileobj = open("info.txt")
except Exception as e:
    print(e)
else:
    print(fileobj)
    # "1- read file content in one string "
    # data = fileobj.read()
    # print(data)
    "2- read file line by line "
    # line = fileobj.readline()
    # print(line)
    #
    # line = fileobj.readline()
    # print(line)
    # fileobj.close()
    "3- read file content into a list"
    # fileobj.seek(10)
    # data = fileobj.readlines(50)  # no of bytes you want to read
    # print(data)

    "4- read file line by line "
    counter = 0
    for l in fileobj:
        if counter==3:
            break
        print(f"line = {l}")
        counter +=1


    fileobj.close()

