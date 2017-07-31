
# 字典的每一个元素都是一个键值对
user_info = {
	"name":"alex",
	"age":73,
	"gender":"M",
}

# 索引
print(user_info['name'])

#输出所有的key为一个列表
print(user_info.keys())
#输出所有的value唯一个列表
print(user_info.values())
# 获取所有的键值对
print(user_info.items())


# 循环 默认输出所有的key 
for i in user_info:
	print(i)
# 循环 输出所有的key 
for i in user_info.keys():
	print(i)
# 循环 输出所有的Value 
for i in user_info.values():
	print(i)


# 循环 所有的itmes
for k, v in user_info.items():
	print(k)
	print(v)

#clear 清除所有的内容

user_info.clear()
print(user_info)


user_info = {
	"name":"alex",
	"age":73,
	"gender":"M",
}

# 根据key 获取值，如果key不存在 可以指定一个默认值
val = user_info.get("age")
print(val)
#key不存在 默认值显示123
val = user_info.get("age111","123")
print(val)
print(user_info["age"])
# 这样获取会出错，推荐用get方法
# print(user_info["age111"])

# has_key 检查字典中指定key是否存在
ret = "age" in user_info.keys()
print(ret)


# update 更新
print(user_info)

dome = {
	"a1":123,
	"a2":456
}
user_info.update(dome)
print(user_info)

# del 删除 删除制定索引的键值对
del dome["a1"]
print(dome)


dic = {"k1":123,"k2":456,"k4":111,}

#从原先字典中找key 生成一个新的字典
n = dic.fromkeys(["k1","k2","k3",], "alex")

print(n)




































