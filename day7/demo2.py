import os

# 路径的拼接
file_path = os.path.join("../day6", "accont", "user.txt")
# print(file_path)

# 判断路径是否存在
if os.path.exists(file_path):
    f = open(file_path, mode="r", encoding="utf-8")
    data = f.read()
    f.close()
    print(data)
else:
    print("Path does not exist.")
