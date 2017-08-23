

import re


# re.match()
# # 从头匹配
# re.search()
# # 浏览全部字符串，匹配第一个符合规则的字符串。
# re.findall()
# # 将匹配到的所有内容都放到一个列表中
# re.finditer()

# # re.split()
# # re.sub()






#不分组
origin = "hello alex lge bcd alex lge alex acd 19"
r = re.match("h\w+", origin)
print(r.group()) # 获取匹配到的所有结果
print(r.groups()) # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组


# 分组  
# 分组是指  提取已经匹配成功的指定内容（先匹配成功全部正则，再把匹配成功的局部内容提取出来）

origin = "hello alex lge bcd alex lge alex acd 19"
# r = re.match("h(\w+)", origin)
r = re.match("(?P<n1>h)(?P<n2>\w+)", origin)
print(r.group()) # 获取匹配到的所有结果
print(r.groups()) # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组

# search
origin = "hello alex lge bcd alex lge alex acd 19"

r = re.search("a(\w+).*(?P<name>\d)$", origin)

print(r.group()) # 获取匹配到的所有结果
print(r.groups()) # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组


# n = re.findall("\d+\w\d+", "a2b3c4d5")
# print(n)
n = re.findall("", "a2b3c4d5")
print(n)


origin = "hello alex lge bcd alex lge alex acd 19"
n = re.findall("a\w+", origin)
n = re.findall("(a\w+)", origin)
n = re.findall("a(\w+)", origin)
n = re.findall("(a)(\w+(e))(x)", origin)
n = re.findall("(a)((\w+)(e))(?P<n1>x)", origin)
print(n)
r = re.finditer("(a)(\w+(e))(?P<n1>x)", origin)
print(r,)
for i in r:
	print(i,i.group(),i.groups(),i.groupdict())

n = re.findall(r"(\d+asd)*", "1asd2asd3asdsdk98jfh")
print(n)

# 贪婪匹配 最后0次
a = "alex"
n = re.findall("(\w)(\w)(\w)(\w)", a)
print(n)
n = re.findall("(\w){4}", a)
print(n)

# 分割
origin = "hello alex lge bcd alex lge alex acd 19"
n = origin.split("a")
print(n)
# 以正则规则进行分割
n = re.split("a\w+", origin)
print(n)

































