
# 居中 第二个参数空白处用*填充
a1 = "alex"
ret = a1.center(20,'*')
print(ret)

# 计算a出现了几次 第二个参数是计算范围
a1 = "alex is alph"
ret = a1.count("al")
ret = a1.count('al',0,5)
print(ret)

# 判断以什么字符结尾
temp = "hello"
# 获取大于等于0的位置，小余2的位置
print(temp.endswith('e',0,2))

#转换table为空格
content = "hello\t999"
print(content)

print(content.expandtabs())

# 查找 如果找到了返回找到的位置，没找到返回-1
s = "alex  hello"
print(s.find("ex"))

# 字符串格式化
s = "hello {0}, age {1}"
print(s)
# # {0} 是占位符
new1 = s.format("alex", 19)
print(new1)

# 查找 如果找到了返回找到的位置，没找到报错
s = "alex  hello"
print(s.index("ex"))

# 连接
li = ["alex","eric"]
# 元祖也可以
li = ("alex","eric")
ret = "_".join(li)
print(ret)

#分割 前中后 三部分，以元组为单位
s = "alex SB eric"
print(s.partition('SB'))

#替换
s = "alex SB alex"
print(s.replace("al","BB",1))

# 从右往左找
s = "alex SB alex"
print(s.rfind("SB"))

# 分割
s = "alexalex"
print(s.split("e"))

#根据换行符进行分割
s = "alex\nalex"
print(s.split("\n"))

#判断某个字符是否是某个字符串开始
s = "alexalex"
print(s.startswith("al"))

# 大写变小写，小写变大写
s = "AlExalEX"
print(s.swapcase())

# 把字符串变成标题
s = "AlExalEX"
print(s.title())
# 把字符串变成大写
s = "AlExalEX"
print(s.upper())





















