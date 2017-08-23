# Author:Da pan

info = {
    'stu1101': 'tenglan wu',
    'stu1102': 'xiaozemaliya',
    'stu1103': 'longzeluola',
}

print(info.get('stu1103'))
print('stu1104' in info)

print(info)
print(info["stu1101"])
info["stu1101"] = "武藤兰"
info["stu1104"] = "苍井空"
print(info)

# del
# del info["stu1101"]
# info.pop("stu1102")
# info.popitem()
# print(info)

for key, value in info.items():
    print(key, value)
for i in info:
    print(i, info[i])
name = input("is time for:")
print(name)
