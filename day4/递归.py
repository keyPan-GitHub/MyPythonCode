



def f1():
	return "F1"

def f2():
	r = f1()
	return r

def f3():
	r = f2()
	return r

def f4():
	r = f3()
	return r


ren = f4()
print(ren)


# 斐波那契数列 前两个相加等于第三个
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657]

def f5(a1,a2):
	if a1 > 10000:
		return
	print(a1)
	a3 = a1 + a2
	return f5(a2,a3)


f5(0,1)



# 写函数 利用递归来获取斐波那契数列的第10个数，并将该值返回给调用者

# def f6(depth,a1,a2):
# 	# print(depth)
# 	if depth == 10:
# 		return a1	
# 	a3 = a1 + a2
# 	return f6(depth + 1,a2,a3)


def f6(depth,a1,a2):
	# print(depth)
	if depth == 10:
		return a1	
	a3 = a1 + a2
	r = f6(depth + 1,a2,a3)
	return r



ret = f6(1,0,1)
print(ret)
























