

# 匿名函数 lambda
def f1():
	return 123

f2 = lambda : 123

r1 = f1()
print(r1)

r2 = f2()
print(r2)


def f3(a1,a2):
	return a1+a2

f4 = lambda a1,a2 : a1+a2


r3 = f3(1,2)
print(r3)

r4 = f4(3,4)
print(r4)


# 内置函数

# 绝对值
i = abs(-123)
print(i)

# all 循环参数，如果每个元素都为真，那么all的返回值为真
# r = all([True,True,False])
# print(r)
# 每个元素都为真True

# 假 0, None, "", [], {}, 空值
# 其他都是真的
r = all(["123", " ", [1,], ""])
print(r)

# any 只有一个为真，则为真
i = any([None,"",[],{},(),123])
print(i)


# ascii 对象的类中找——repr——方法，获取其返回值

class foo:
	def __repr__(self):
		return "hello"

obj = foo()
r = ascii(obj)
print(r)


# 进制转换
# bin()	#二进制
i = bin(11)
print(i)
# oct()	#八进制
i = oct(11)
print(i)
# int()	#十进制
i = int(11)
print(i)
# hex()	#十六进制
i = hex(11)
print(i)

# 其他进制转换成十进制

r = int("0x110",base=16)
print(r)

# bool 判断真假，把一个对象转换成布尔值，None,"",[],{}

# str
# list

# bytes		字节
# bytearray		字节列表[zijie]

# str转字节码
# bytes["xxxx",encoding="utf-8"]

# assic 转换
# chr()
# ord()

# 一个字节8位，2**8 256: A B c ( _
# assic 转 字符
r = chr(97)
print(r)
# 字符 转 assic
r = ord("a")
print(r)

# 生成一个随机数
# 一个数字转换成字母：chr()

import random

# 纯字母
temp = ""
for i in range(6):
	rad1 = random.randrange(65, 91)
	c1 = chr(rad1)
	temp = temp+c1

print(temp)



temp = ""
for i in range(6):
	#6次循环生成6次随机数，每次四种可能
	num = random.randrange(0, 4)
	#如果随机数恰好符合条件1或者3，就生成数字，不符合就生成字母，
	if num == 3 or num == 1:
		rad2 = random.randrange(0, 10)
		temp = temp + str(rad2)
	else:
		rad1 = random.randrange(65, 91)
		c1 = chr(rad1)
		temp = temp+c1

print(temp)


# callable() 是否可执行

def f1():
	return 123

f1()
f1 =123
r = callable(f1)
print(r)

# 编译一个大的字符串代码 编译字符串里的代码
# compile("""
# def f1():
# 	return 123
# """)

# dir() 查看功能
li = []
print(dir(li))

# 帮助
help(li)


a = 10 / 3
print(a)
# 能得到一个商和余数的元组
r = divmod(10,3)
print(r)

# compile 编译 字符串形式的代码
# eval 有返回值 处理字符串形式的表达式用eval
# exec 执行 字符串形式的代码
a = 1 + 3
print(a)

a = "1 + 3"
print(a)
# 处理字符串形式的表达式用eval
a = eval("1 + 3 + 5")
print(a)
ret = eval("a + 66",{"a":99})
print(ret)

# exec 执行简单的字符串包裹代码
exec("for i in range(10) : print(i)")

# 筛选
# 循环可迭代的对象，获取每一个参数，函数（参数）
# filter(函数，可迭代的对象)

def f1(x):
	# if x > 22:
	# 	return True
	# else:
	# 	return False
	return x > 22

f2 = lambda x : x > 22
ret = filter(f2, [11,22,33,44])

# 匿名
ret = filter(lambda x : x > 22, [11,22,33,44])

for i in ret:
	print(i)


# map(函数,可迭代对象)

def f3(x):
	return x + 100

ret = map(f3,[1,2,3,4,5])

print(ret)
for i in ret:
	print(i)

# 匿名
ret = map(lambda x : x + 100,[1,2,3,4,5])
print(ret)
for i in ret:
	print(i)

def f3(x):
	if x % 2 == 1:
		return x + 100
	else:
		return x

# 筛选奇数
ret = map(lambda x : x + 100 if  x % 2 == 1 else x,[1,2,3,4,5])
print(ret)
for i in ret:
	print(i)

# 获取当前代码的所有的全局变量
# globals()
# 获取所有的局部变量
# locals()

def f1():
	name = 123
	print(globals())
	print(locals())

f1()

li = [11,22,33]
# 判断某个对象是否由某个类创建的
r = isinstance(li,list)
print(r)

# 最大值与最小值
li = [11,22,123]
r = max(li)
print(r)
r = min(li)
print(r)


# 求指数的 pow()

i = pow(2,31)
print(i)

#四舍五入

r = round(3.6)
print(r)

# 求和
r = sum([11,22,33])
print(r)


li1 = [11,22,33,44]
li2 = ["a","BB","c","d"]

r = zip(li1,li2)
print(r)
for i in r:
	print(i)


# 排序 想排序只能同一种类型
li = [171,424,353,262,321]
print(li)
# 作用于自身
li.sort()
print(li)

li = [1,2,5,89,123,54]
# 拿到一个排序后新的值
news_li = sorted(li)
print(news_li)






























