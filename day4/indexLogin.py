


def login(username,password):
	"""
	用于用户名与密码的验证
	:param username: 用户名
	:param password: 密码
	:return: True，用户名验证成功，False，用户验证失败
	"""

	f = open("db.txt","r",encoding="utf-8")
	for line in f:
			#切掉换行符
			#默认strip无参数，空格，换行符
			#有参数：移除两侧指定的值
		line = line.strip()
			#按$分割成列表
		line_list = line.split("$")
		if username == line_list[0] and password == line_list[1]:
			# print("登录成功")
			return True
	return False


def register(username,password):
	"""
	注册用户
	1，打开文件
	2. 用户名$密码

	:param username: 用户名
	:param password: 密码
	:return: True，注册成功
	"""
	with open("db.txt","a",encoding="utf-8") as f:
		temp = "\n" + username + "$" + password
		f.write(temp)
	return True


def user_exist(username):
	"""
	检查用户名是否存在
	:param username: 要检测的用户名
	:return: True，用户名已经存在，False，用户不存在
	"""
	# 一行一行的查找，如果用户名存在，return True ：False

	with open("db.txt","r",encoding="utf-8") as f:
		for line in f:
			# 去除换行符与空白
			line = line.strip()
			# 分割
			line_list = line.split("$")
			if line_list[0] == username:
				return True
	return False


def main():
	"""
		主函数
	"""
	print("欢迎登录xxx系统")
	inp = input("1: 登录；2：注册")

	user = input("请输入用户名")
	pwd = input("请输入密码")

	if inp == "1":
		is_login = login(user, pwd)
		if is_login:
			print("登录成功")
		else:
			print("登录失败")
	elif inp == "2":
		is_exist = user_exist(user)
		if is_exist:
			print("用户名已经存在,无法注册")
		else:
			result = register(user, pwd)
			if result:
				print("注册成功")
			else:
				print("注册失败")




main()


















