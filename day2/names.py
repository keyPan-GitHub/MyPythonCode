# Author:Da pan

import copy

names = ["zhangyang","guyun","xiangpeng",["alex","jack"],"xuliangchen","xiedi"]

names.append("leihaidong")
names.insert(1,"chenronghua")
names.insert(3,"xiezhiyu")
names[2] = "xiedi"
print(names)

# delete
names.remove("chenronghua")
del names[2]
names.pop()
print(names)

# 查找
print(names.index("xiedi"))
print(names[names.index("xiedi")])

# 统计
print(names.count("xiedi"))
# names.clear()
print(names)
names.reverse()
print(names)
# names.sort()
print(names)
names2 = [1,2,3,4]
# 合并
names.extend(names2)
print(names,names2)

# 复制




#浅复制
# names3 = names.copy()
#深复制
names3 = copy.deepcopy(names)

print(names)
print(names3)
names[1] = "谢迪"
names[2][1] = "JACK"
print(names)
print(names3)