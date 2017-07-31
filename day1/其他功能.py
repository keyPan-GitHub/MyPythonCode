li = ["电脑","鼠标垫","u盘","游艇"]

# for key,item in enumerate(li,1):
# 	print(key,item)

# inp =  input("请输入商品：")

# inp_num = int(inp)

# print(li[inp_num-1])

# # 输入汉字查索引
# inp = input("请输入商品：")
# ret = li.index(inp)
# print(ret)

print(range(1,10))
for i in range(1,10):
	print(i)
print("------------------")
for i in range(1,10,2):
	print(i)
print("------------------")
for i in range(10,1,-1):
	print(i)
print("------------------")
for i in range(10,1,-2):
	print(i)
print("------------------")
for i in range(0,-10,-1):
	print(i)

#字符串与bytes类型互相转化

li = ["alex","eire"]

leee = len(li)

for i in range(0,leee):
	print(i,li[i])

a = "李璐"

b1 = bytes(a,encoding="utf-8")
print(b1)
b2 = bytes(a,encoding="gbk")
print(b2)

newa1 = str(b1,encoding="utf-8")
print(newa1)

newa2 = str(b2,encoding="gbk")
print(newa2)


dic = {"k1":123,"k2":456,"k4":111,}

#从原先字典中找key 生成一个新的字典
n = dic.fromkeys(["k1","k2","k3",], "alex")

print(n)

n1 = {"k1":[],"k2":[],"k4":[],}
print(n1)
# 只有第一个列表添加了x
n1["k1"].append("x")
print(n1)

n2 = dic.fromkeys(["k1","k2","k3",], [])
print(n2)
# 所有的列表都添加了x 
# 原来我们创建列表每个元素单独对应一个列表
# 而通过fromkey（）创建的三个元素对应一个列表
n2["k1"].append("x")
print(n2)







