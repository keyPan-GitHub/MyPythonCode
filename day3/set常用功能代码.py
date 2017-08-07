
se = {11,22,33}
# set 输出无序
print(se)

se.add(44)
print(se)

se.clear()
print(se)


se = {11,22,33}

be = {22,55}

# 寻找se中存在，be中不存在的集合
se.difference(be)
# 寻找be中存在，se中不存在的集合
be.difference(se)

print(se)
# 寻找se中存在，be中不存在的集合 并将其赋值给新变量
ret = se.difference(be)
print(ret)

se.difference_update(be)
# 寻找se中存在，be中不存在的集合,更新自己,把寻找到的值重新赋值给自己
print(se)


se = {11,22,33}
# 移除自身某个元素，不存在不报错
se.discard(11)
print(se)


se = {11,22,33,44}
be = {22,59,"随便"}
# 交集，两个set中都有的就叫交集 获得的交集赋值给新变量
ret = se.intersection(be)
print(ret)
# 交集，两个set中都有的就叫交集 把交集重新赋值给自己，更新自己，
se.intersection_update(be)
print(se)


se = {11,22,33,44}
be = {22,59,"随便"}
# 有交集是Flase 没有交集是True 判断两个集合有没有交集 
ret = se.isdisjoint(be)
print(ret)

se = {11,22,33,44}
be = {11,22}
# 判断se是不是be的父序列
ret = se.issuperset(be)
print(ret)

# 判断se是不是be的子序列
ret = se.issubset(be)
print(ret)

# 移除元素并返回给新值
ret = se.pop()
print(ret)
print(se)


se = {11,22,33,44}
be = {11,22,77,55}
#并集
ret = se.union(be)
print(ret)

# 更新
se.update(be)
print(se)

se.update([444,555,666,777])
print(se)

# 差集
r1 = se.difference(be)
r2 = be.difference(se)
print(r1)
print(r2)
# 对称交集 相当于把不同的并一块
ret = se.symmetric_difference(be)
print(ret)
# 谁调用的把谁更新成对称交集
se.symmetric_difference_update(be)
print(se)






































