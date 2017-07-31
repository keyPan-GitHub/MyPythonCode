# Author:Da pan

school = "oldboy edu"

def change_name(name):
    global school
    school = "MaGe Linux"
    print("before name ",name,school)
    name = "Da Pan"
    # age = 23
    print("after name %s" % name)

name = "da pan"
change_name(name)
print(name)
print(school)


