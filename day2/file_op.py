# Author:Da pan
'''
# date = open('yesterday',encoding="utf-8").read()
f = open('yesterday2','a',encoding="utf-8") #文件句柄

f.write("\n when i was young i listen to the radio")
data = f.read()
print('---read',data)

with f as file_objc:
    file_objc.write("\n when i was young i listen to the radio\n")

f.close()
'''

# f = open('yesterday2','r+',encoding="utf-8") #文件句柄 读写
# f = open('yesterday2','w+',encoding="utf-8") #文件句柄  写读
# f = open('yesterday2','a+',encoding="utf-8") #文件句柄  追加读写
# f = open('yesterday2','rb') #文件句柄  二进制文件 读
f = open('yesterday2', 'wb')  # 文件句柄  二进制文件 写

f.write("hello binary\n".encode())
f.close()

'''
f.write("--------------diao--------------1\n")
f.write("--------------diao--------------1\n")
f.write("--------------diao--------------1\n")
f.write("--------------diao--------------1\n")
print(f.tell())
f.seek(10)
print(f.tell())
print(f.readline())
f.write("should be at the begining of the second line")
f.close()
'''

'''
print(f.tell())
# print(f.read(5))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
print(f.encoding)
print(f.fileno())

print(f.flush())
print(f.buffer)
f.seek(10)
f.truncate(20)

'''
# high bige
'''
count = 0
for line in f:
    if count == 9:
        print('----------------我是分隔符----------------')
        count += 1
        continue
    print(line)
    count += 1
# low loop

for index,line in enumerate(f.readlines()):
    if index == 9:
        print('----------------我是分隔符----------------')
        continue
    print(line.strip())

# for i in range(5):
    # print(f.readline())
'''
