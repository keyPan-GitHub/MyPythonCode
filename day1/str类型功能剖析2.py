#判断 是不是 字母和数字
a = "abc9"
print(a.isalnum())

#判断 是否 都是 字母
a = "abc"
print(a.isalpha())


#判断 是否 都是 数字
a = "9999"
print(a.isdigit())

#判断 是否 都是 小写
a = "alex"
print(a.islower())

#判断 是否 都是 空格
a = "    "
print(a.isspace())

#判断 是不是 标题
a = "Alex"
print(a.istitle())

#判断 是不都是 大写
a = "ALEX"
print(a.isupper())

#左对齐，右侧填充
a = "alex"
print(a.ljust(20,"*"))


#右对齐，左侧填充
a = "alex"
print(a.rjust(20,"*"))

# 把字符串变小写
a = "ALEX_ERIC"
print(a.lower())

# 移除左侧的空格
a = " alex "
print(a.lstrip())

# 移除右侧的空格
a = " alex "
print(a.rstrip())

# 移除两侧的空格
a = " alex "
print(a.strip())














