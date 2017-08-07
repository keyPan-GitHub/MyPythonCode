
# def f1(a):
# 	print(a,type(a))

# f1(123)
# f1("123")
# f1([11,22,33,44])

# 动态参数
# def f1(*a):
# 	print(a)

# f1(123,"123",[11,22,33],{"k1":"v1"})


# def f1(**a):
# 	print(a)

# f1(k1=123,k2=456)

# 动态参数 两者结合的

# def f1(p, *args, **kwargs):
# 	print(p,type(p))
# 	print(args,type(args))
# 	print(kwargs,type(kwargs))

# f1(11,22,33, k1=123,k2=456)


# def f1(*args):
# 	print(args,type(args))

# li = (11,22,33,44)
# f1(li,"123")
# f1(*li,"123")


# def f1(**kwargs):
# 	print(kwargs,type(kwargs))

# dic = {
# 	"k1":123,
# 	"k2":456,
# }
# f1(k1=dic)
# f1(**dic)



# 全局变量与局部变量

PERSON = "alex"

def f1():
	# 局部变量 a 只在这里能用 
	a = 123
	global PERSON
	PERSON = "eric"	
	print(a)

def f2():
	a = 456
	print(PERSON)
	print(a)


f1()
f2()


def fi(args):
	# 函数的参数都是引用
	# 原先的 args = li 所以 args是可以修改li的值的，因为两者指向的是同一块内存地址
	# args.append(123)
	if len(args) > 2:
		del args[2:]
	args = 123
li = [11,22,33,44]
fi(li)
print(li)


def fi(args):
	# 参数值重新指向了新的一块内存地址
	args = 123
li = [11,22,33,44]
fi(li)
print(li)

# 一旦变量遇到等号
# naem = xxxx
# 如果xxxx = 真实的值 ，内存创建
# 如果xxxx = 变量 ，指向变量的内存


