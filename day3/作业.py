"""
li = [11,22,33,44,55,66,77,88,99,90]
l1 = []
l2 = []

dict = {"k1":[],"k2":[]}
for i in li:
	if i <= 66:
		dict["k1"].append(i)
	else:
		dict["k2"].append(i)
# dict = {"k1":l1,"k2":l2}
print(dict)

li = ("aleb"," aric","Alex","Tony","rain")

for i in li:
	new_i = i.strip()
	if (new_i.startswith('a') or new_i.startswith('A')) and new_i.endswith("c"):
		print(new_i)
"""


"""
li = ["手机","电脑","鼠标垫","游艇"]

for i,j in enumerate(li):
	print(i+1,j)

num = input("name")
# 索引
number = int(num)
len_li = len(li)
if number > 0 and number <= len_li:
	good = li[number - 1]
	print(good)
else:
	print("shopping not care")
"""


"""
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "郑州": ["郑大","少林寺","嵩山"],
        "开封": ["包拯","展少侠","武当山"],
    },
    "山西": {
        "太原": ["xxx","ooo","小店"],
        "运城": ["999","秋林红肠","哈尔滨啤酒"],
    }
 
}


for x in dic:
	print(x)

i1 = input("请输入省份")
a = dic[i1]

for j in a:
	print(j)

i2 = input("请输入省份")
b = dic[i1][i2]

for z in b:
	print(z)
"""

"""
asset_all = 0
car_list = []
i1 = input("请输入总资产：")

asset_all = int(i1)

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]


for i in goods:
	# i 每个列表的元素 字典
	print(i["name"],i["price"])

while True:
	i2 = input("请输入购买的商品(Y/y 结算):")
	# 
	if i2.lower() == "q":
		break
	for j in goods:
		if j["name"] == i2:
			# print(j)
			car_list.append(j)

	print(car_list)

# 结算
all_price = 0
for item in car_list:
	p = item["price"]
	all_price += p
print(asset_all,all_price)

if all_price > asset_all:
	print("穷逼")
else:
	print("购买成功")
"""


asset_all = 0

car_dict = {}
# car_dict = {
# 	"电脑":{"price":单价,"num":123}
# }
i1 = input("请输入总资产：")
asset_all = int(i1)

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

for i in goods:
	# i 每个列表的元素 字典
	print(i["name"],i["price"])

while True:
	i2 = input("请选择商品:")
	if i2.lower() == "q":
		break
	for item in goods:
		if item["name"] == i2:
			# item = {"name": "电脑", "price": 1999},
			name = item["name"]
			# 判断购物车是否有该商品
			if name in car_dict.keys():
				# pass
				car_dict[name]["num"] = car_dict[name]["num"]+1
			else:
				car_dict[name] = {"num":1,"single_price":item["price"]}

print(car_dict)


	# {'电脑': 
	# 	{'num': 21, 'single_price': 1999}, 
	# '美女': 
	# 	{'num': 7, 'single_price': 998}}

all_price = 0

for k,v in car_dict.items():
	n = v["single_price"] 
	m = v["num"]
	all_sum = m*n
	all_price += all_sum

if all_price > asset_all:
	print("穷逼")
else:
	print("购买成功")









