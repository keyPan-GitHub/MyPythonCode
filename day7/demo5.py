import random


# 生成一个10到99之间的随机整数
v1 = random.randint(10, 99)
print(v1)

# 生成一个随机的六位验证码数字
v2 = random.randrange(100000, 999999)
print(v2)

# 生成四位的随机的字母
for i in range(4):
    v3 = chr(random.randint(65, 90))
    print(v3, end="")
