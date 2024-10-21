import os

# 创建一个文件夹，用于存储用户名和密码
# 输入用户名和密码
user = input("Enter your username: ")
password = input("Enter your password: ")

# 字符串格式化
formatted_string = f"Username: {user}, Password: {password}"

# 指定文件路径参数
fileder_path = os.path.join("output", "credentials")

# 确保目录存在，如果不存在则创建
if not os.path.exists(fileder_path):
    os.makedirs(fileder_path)

# 拼接文件夹路径
file_path = os.path.join(fileder_path, "user.txt")

# 打开文件，写入格式化后的字符串
with open(file_path, "a", encoding="utf-8") as file:
    file.write(formatted_string)
    print("Credentials saved to output/credentials.txt")
