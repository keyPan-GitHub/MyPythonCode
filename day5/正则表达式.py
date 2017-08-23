


import re

# search 代表只找到一个就不找了。
# findall 寻找所有的
# match 只会匹配开头那个部分

# 基本匹配
r = "abcd".find('b')
print(r)

r = "abcd".find('bc')
print(r)

r = "abcd".split("b")
print(r)

r = "abcd".replace("ab", "ee")
print(r)

r = "askdjh127.0.0.1dsajklghdf"

# 正则匹配
# 完全匹配，把所有的结果拿到以列表输出
r = re.findall('alex', 'yanaleSxalexwupeiqi')
print(r)

r = re.findall('alex', 'yanaleSxalwexwupeiqi')
print(r)

# 元字符 · 重点
# 元字符 · 通配符，代指除了换行符之外的任何字符，都可以匹配
r = re.findall('alex.w', 'aaaaalexaw')
print(r)
r = re.findall('alex.w', 'aaaaalexsw')
print(r)
# 一个·只能匹配一个字符
r = re.findall('alex.w', 'aaaaalexbbw')
print(r)

# ^ - 尖角符 控制开头
# ^ - 尖角符 代表 要配备的条件必须在开头
r = re.findall('^alex', 'yanaleSxalexwupeiqi')
print(r)

r = re.findall('^alex', 'yanaleSx^alexwupeiqi')
print(r)

r = re.findall('^alex', 'alexyanaleSxalexwupeiqi')
print(r)

# $ 美刀符 控制结尾的
# $ 美刀符 代表 要配备的条件必须在结尾
r = re.findall('alex$', 'alexyanaleSxalexwupeiqi')
print(r)

r = re.findall('alex$', 'alexyanaleSxalexwupeiqialex')
print(r)

# * + ？ {}  他们都在做一件事情 ，重复

# * 代表匹配0到多次 0-n次 表示0次也可 多次也可 
#	但是只能匹配相邻的之前1个字符  贪婪匹配
r = re.findall('alex*', 'wwwwalex')
print(r)

r = re.findall('alex*', 'wwwwalexxxxxx')
print(r)

r = re.findall('alex*', 'wwwwale')
print(r)


# + 代表匹配1到多次 1-n次 表示1次也可 多次也可 0次不可
#	但是只能匹配相邻的之前1个字符  贪婪匹配
r = re.findall('alex+', 'wwwwalex')
print(r)

r = re.findall('alex+', 'wwwwalexxxxxx')
print(r)

r = re.findall('alex+', 'wwwwale')
print(r)

# ？ 代表匹配0到1次 0-1次 表示1次也可 0次也可 多次就出现1个
r = re.findall('alex?', 'wwwwale')
print(r)

r = re.findall('alex?', 'wwwwalex')
print(r)
# 多次也就显示1次那个
r = re.findall('alex?', 'wwwwalexxxxx')
print(r)


# {} 代表匹配固定次数，自己设置
r = re.findall('alex{3}', 'wwwwalexxx')
print(r)
# 少了不行
r = re.findall('alex{3}', 'wwwwalexx')
print(r)
# 多了不要
r = re.findall('alex{3}', 'wwwwalexxxx')
print(r)

# 闭区间 3-5 个都可以
r = re.findall('alex{3,5}', 'wwwwalexxxx')
print(r)


# 【】字符集
r = re.findall('a[bc]d', 'wwwabd')
print(r)
r = re.findall('a[bc]d', 'wwwacd')
print(r)
r = re.findall('a[bc]d', 'wwwacdabd')
print(r)
# []里面的bc是 或者，不是并列的意思所有两者只能取其一
r = re.findall('a[bc]d', 'wwwabcd')
print(r)

# · 元字符在字符集中没有意义
r = re.findall('a[.]d', 'wwwaqd')
print(r)

r = re.findall('a[.]d', 'wwwa.d')
print(r)

# 匹配小写 a到z  
r = re.findall('[a-z]', 'wwwa.d')
print(r)

r = re.findall('[A-Z]', 'wWwaDqW')
print(r)

r = re.findall('[1-9]', 'wWw3Sa5D7qW')
print(r)
# ^ 尖角符  在字符集中^代表 “非” 的意思 取反 除了1-9 剩下的都取
r = re.findall('[^1-9]', 'wWw3Sa5D7qW0')
print(r)

# 最重要的元字符 \:			
		# 反斜杠后边跟元字符去除特殊功能
		# 反斜杠后边跟普通字符实现特殊功能
		# 引用序号对应的字组所匹配的字符串

# \d  	匹配任何十进制数，他相当于类 【0-9】
# \D 	匹配任何非数字字符，他相当于类 【^0-9】
# \s 	匹配任何非空白字符，他相当于类	【 \t\n\r\f\v】
# \S 	匹配任何非空白字符，他相当于类	【^ \t\n\r\f\v】
# \w 	匹配任何非字母数字字符，他相当于类 	【a-zA-Z0-9】
# \W 	匹配任何非字母数字字符，他相当于类	【^a-zA-Z0-9】
# \b:	匹配一个单词边界，也就是指单词和空格间的位置 
r = re.findall(r"\babc\b", "abc asadsdasdasdasdsadasd")
# \d
r = re.findall(r'\d', 'wWw3Sa5D7qW0')
print(r)
# \d 代表一个字符 10以上要多个
r = re.findall(r'\d\d', 'wWw3Sa15D7qW0')
print(r)
# \w 
r = re.findall(r'\w', 'wWw3Sa15D7q.W0')
print(r)
# \s
r = re.findall(r'\s', 'wW\nw\t3Sa 15 D7q.W 0')
print(r)
# \d 在字符集中还是具有特殊功能
r = re.findall(r'[\d]', 'wWw3Sa15D7q.W0')
print(r)


# () 组的概念，把括号内视为整体、
r = re.findall(r'(ab)*', 'aba')
print(r)


r = re.search(r"(ab)*", "aba").group()
print(r)

r = re.search(r"alex", "abaalexalex").group()
print(r)
# 沒匹配到就返回None 匹配到会返回match——object对象
r = re.match("alex", "abaalexalex")
print(r)

# 贪婪模式
r = re.search(r"a(\d+)", "a234749873167basd").group()
print(r)
# 非贪婪模式
r = re.search(r"a(\d+?)", "a234749873167basd").group()
print(r)

r = re.search(r"a(\d*?)", "a234749873167basd").group()
print(r)

# 在括号前后都有限定条件的时候，变成非贪婪模式
r = re.findall(r"a(\d+?)b", "a2314654674b")
print(r)

r = re.search(r"a(\d+?)b", "a234749873167b").group()
print(r)


# 引用序号对应的字组所匹配的字符串
# (alex)(eric)com\2 = alexericcomeric  \2 取出第二个括号里的
r = re.search(r"(alex)(eric)com\2", "alexericcomeric").group()
print(r)

# re.I 		使其不区分大小写
# re.L		做本地化识别(locale-aware)匹配
# re.M 		多行匹配，影响^和$
# re.S 		使·匹配包括换行符在内的所有字符
# re.U 		根据Unicode字符集解析字符，这个标志影响 \w \W \b
# re.X 		该标志通过给与你更灵活的格式以便你将正则表达式写得更
# re.I   第三个参数改变了正则的工作模式，使其不区分大小写

r = re.search("com", "COM",re.I).group()
print(r)
# 普通的区分大小写
# r = re.search("com", "COM").group()
# print(r)

r = re.findall(".", "abc\nde")
print(r)


# 替换
r = re.sub("g.t", "have", "I get A, I got B, I gut C",2)
print(r)

r = re.findall(r"\\", "asdsad\som")
print(r)


r = re.match(r'\bblow', "blow")
print(r)














































































