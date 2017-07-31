name_tuple = ('alex','eric')

# 索引
print(name_tuple[0])
# len
print(name_tuple[len(name_tuple)-1])
# 切片
print(name_tuple[0:1])
# for循环
for i in name_tuple:
	print(i)

# 删除 (不支持)
# del name_tuple[0]

# count 计算元素出现的个数
print(name_tuple.count("alex"))

# index 获取元素的索引位置
print(name_tuple.index("alex"))

t = (11,22,["alex",{"k1":"v1"}])
t[2][1]["k1"] = "b1"
t[2].append("xxxx")
print(t)

# 字典添加方法
dic = {"k1":"v1"}
dic.update({"k2":"v2"})
print(dic)
dic["k3"] = 123
print(dic)



