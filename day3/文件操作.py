

# 文件操作
# 操作文件
# 关闭文件



# open("文件名","模式","编码")
# 默认是只读模式
# f = open("ha.log")
# data = f.read()
# f.close()
# print(data)

# 只读 R 不能写
# f = open("ha.log","r")
# f.write("12314654")
# f.close()

# 只写 w 不可读
# f = open("ha.log","w")
# f.read()
# f.close()
# 【不可读，文件不存在则创建 存在则清空】
# f = open("ha1.log","w")
# f.write("1234654987")
# f.close()

# x模式 写模式，【 不可读 文件不存在则创建 存在则报错】
# f = open("ha2.log","x")
# f.write("asdasd")
# f.close()

# 追加模式 a 【 不可读 文件不存在则创建 存在则只追加内容】
# f = open("ha2.log","a")
# f.write("6666")
# f.close()


# 以字节方式打开
# 只读，二进制打开只读，rb
# f = open("ha.log","rb")
# data = f.read()
# f.close()
# print(data)
# print(type(data))

# str_data = str(data,encoding="utf-8")
# print(str_data)

# 只写 wb 二进制方式写入
# f = open("ha.log","wb")
# str_data = "日本"
# bytes_data = bytes(str_data,encoding="utf-8")
# f.write(bytes_data)
# f.close()


# 普通打开
# Python内部将01010101二进制编码转换成字符串 通过字符串操作
# 010101010     ---字节---    Python解释器	---字符---	程序员

# 二进制打开方式

# r+ 读写
# W,末尾追加，指针最后
# f = open("ha.log","r+",encoding="utf-8")
# #指针起始位置
# print(f.tell())

# data = f.read(1)
# print(type(data),data)

# print(f.tell())

# f.write("SB")

# #指针终止位置
# print(f.tell())
# f.seek(0)

# data = f.read()
# print(type(data),data)
# f.close()



# w+ 写读
# 先清空，然后读取的是写之后的（在写之后，可以读）
# 先清空，我之后写的才可以读，写，指针到最后
# f = open("ha.log","w+",encoding="utf-8")
# f.write("何莉莉")
# f.seek(0)
# data = f.read()
# f.close()

# print(data)


# a+ 打开的同时，指针已经移动到最后
# 写的时候，追加，放到最后
f = open("ha.log","a+",encoding="utf-8")
print(f.tell())
f.write("sb")
# data = f.read()
# print(data)

# f.seek(0)

# data = f.read()
# print(data)


# f.tell() # 获取指针位置
# f.seek() # 调整指针位置
# f.write() #写入
# f.read() # 读取

f.close()



