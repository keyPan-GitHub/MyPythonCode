

n1 = 123
n2 = n1
print(id(n1))
print(id(n2))

import copy

n1 = 123
n2 = copy.copy(n1)
print(id(n1))
print(id(n2))

n2 = copy.deepcopy(n1)
print(id(n1))
print(id(n2))

n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
n2 = copy.copy(n1)
# 浅拷贝第一层不一样，
print(id(n1),id(n2))
# 浅拷贝第二层内存地址相同
print(id(n1["k1"]),id(n2["k1"]))
print(id(n1["k3"]),id(n2["k3"]))
