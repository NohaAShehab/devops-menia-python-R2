""" simple text files
    write content the file

    ---> open file with mode a  ---> starting from the end of the file


    ===> if file doesn't exist ---> will try create it.

"""
try:
    fileobj = open("info/mycv.txt", "a")
except Exception as e:
    print(e)
else:
    # "write file "
    # print(fileobj)
    # fileobj.write("My name is Noha\n")
    # fileobj.write("I lives in cairo\n")
    # "seek posistion"
    # fileobj.seek(10)
    # fileobj.write("--------------------------")
    fileobj.writelines(["Ahmed\n", "iti\n", "Devops\n", "python\n"])

    fileobj.close()

