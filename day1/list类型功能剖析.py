
name = "alex"

age = 18

name_list = ["eirc","alex","tony"]
# 索引
print(name_list[0])
print(name_list[0:2])
print(name_list[2:len(name_list)])

for i in name_list:
	print(i)

# 向后添加
name_list.append("seven")
name_list.append("seven")
# 按字符查找有几个 元素出现的次数
print(name_list)
print(name_list.count("seven"))

# 批量添加
temp = [111,222,333,444]
name_list.extend(temp)
print(name_list)

# 获取某个元素的索引
print(name_list.index("alex"))

# 在指定个索引的位置插入
name_list.insert(1,"SB")
print(name_list)

# 移除最后一个元素 赋值给另外一个
a1 = name_list.pop()
print(name_list)
print(a1)

# 移除某个元素
name_list.remove("seven")
print(name_list)

# 删除指定元素 根据索引删除
print(name_list)
del name_list[1]
del name_list[1:3]
print(name_list)

# 反转
name_list.reverse()
print(name_list)

#排序 跟算法一起学
# name_list.sort()
# print(name_list)

# 转换
# 列表转列表
t = [11,22,33,44]
li = list([11,22,33,44])
print(li)

#字符串转换成列表
s1 = "李路"
l1 = list(s1)
print(l1)

#元祖转换成列表
s2 = ("alex","laonanhai","seven")
l2 = list(s2)
print(l2)

#字典
dic = {'k1':"alex",'k2':"seven"}
l3 = list(dic.keys())
print(l3)
l3 = list(dic.values())
print(l3)
l3 = list(dic.items())
print(l3)

# 添加在自身原本的变量上。
li = list()
li.append(1)
print(1)
# 添加在一个新的变量上
s = "alex "
s.strip()
news = s.strip()
#原本的s还带有空格
print(s)
#复制给新的变量的没有空格了
print(news)


li = [11,22,33,44]
dic = {}
for i,j in enumerate(li,10):
	dic[i] = j
	print(j)
print(dic)

news_dic = dict(enumerate(li,10))
print(news_dic)







