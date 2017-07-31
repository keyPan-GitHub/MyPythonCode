# Author:Da pan

# import sys

# 打印环境变量
# print(sys.path)
# 打印相对路径。
# print(sys.argv)


import os,sys

# cmd_res = os.system("dir") #执行命令，但是保存结果。输出0证明成功运行
cmd_res = os.popen("dir").read()
print("-->",cmd_res)

name = {'1':'2','2':'1'}

for i in name:
	print(i,name[i])
