
def MyFilter(func, seq):
	# func 函数名，函数名() ==>执行函数
	# seq 循环
	result = []
	for i in seq:
		print(i)
		# func == f1
		# func() 执行f1函数，并获取其返回值，将其赋值给ret
		ret = func(i)
		if ret:
			result.append(i)

	return result

def f1(x):
	if x > 22:
		return True
	else:
		return False

r = MyFilter(f1, [11,22,33,44])

print(r)


def MyMap(func,arg):
	# func ==》 代指函数
	# arg ==》 li列表
	result = []
	for i in arg:
		ret = func(i)
		result.append(ret)
	return result

li = [11,22,33,44]

def f2(arg):
	return arg + 100

r = MyMap(f2,li)

print(r)



















