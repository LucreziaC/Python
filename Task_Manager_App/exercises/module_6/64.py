new_member = input("Enter a new member: ")
file = open("exercises/module_6/files/members.txt", "r")
members = file.readlines()
members.append(new_member)
file.close()

file = open("exercises/module_6/files/members.txt", "w")
file.writelines(members)
file.close()
