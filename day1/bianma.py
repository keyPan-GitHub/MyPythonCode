# -*- coding:utf-8 -*-

temp = "理解"

# temp_unicode = temp.decode("utf-8")
temp_gbk = temp.encode("gbk")
temp_unicode = temp_gbk.decode("gbk")

print(temp_unicode)

# s = "Alex SB"
# ret = "SB" in s
# print(ret)

li = ['alex',"eric","rain"]
ret = "alex" not in li
print(ret)