# Author:Da pan

print("hello world")

name = "Da pan"

print("My Name is",name)

# username = input("username:")
# password = input("password:")
# print(username,password)
name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")

info = '''
----------------info of %s----------------
Name:%s
age:%d
job:%s
salary:%s
''' % (name,name,age,job,salary)


info2 = '''
----------------info of {_name}----------------
Name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name = name,
           _age = age,
           _job = job,
           _salary = salary)

print(info2)