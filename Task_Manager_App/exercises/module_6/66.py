files= [open("exercises/module_6/files/a.txt", "r"),open("exercises/module_6/files/b.txt", "r"),open("exercises/module_6/files/c.txt", "r") ]
for file in files:
    print(file.readline())
    file.close()