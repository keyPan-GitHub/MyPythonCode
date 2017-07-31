# Author:Da pan



name = "my \tname is {name} and i am {year} old"

print(name.capitalize()) #首字母大写
print(name.upper()) #字母大写
print(name.count("a")) #统计有多少个a字
print(name.center(50,"-")) #打印50个字符不够的用-补上 把name放在中间
print(name.endswith("ex")) #判断一段字符串以什么结尾
print(name.expandtabs(tabsize=30)) #把tab键转换成字符
print(name.find("name")) #查找字符串索引
print(name[name.find("name"):]) #字符串切片
print(name.format(name='alex',year=23))
print(name.format_map({'name':'alex','year':'12'}))
print("ab23".isalnum()) #判断是否是阿拉伯数字（包含英文与数字，不包含特殊字符）
print("ab23\!".isalnum())
print("abA".isalpha()) #大小写英文
print("1A".isdecimal()) # 判断是否是十进制
print("1A".isdigit()) #判断是否是一个整数
print("1A".isidentifier()) #判断是不是一个合法的标识符（是不是合法的变量名）
print("1A".islower()) #判断是否是小写
print("33".isnumeric()) # 判断是否是只有数字（小数浮点数不可以）
print("33A".isspace()) #判断是否是一个空格
print("My Name Is".istitle()) # 首字母大写
print("My Name Is".isprintable()) #tty file,drive file
print("My Name Is".isupper()) #判断是不是全文大写
print('+'.join(['1','2','3','4',])) #把列表变成字符串
print(name.ljust(50,"*")) #长度50 不够的话用星号在右面补全
print(name.rjust(50,"-")) #长度50 不够用星号左面补全
print("ALEX".lower()) #把大写变成小写
print("alex".upper()) #把小写变成大写
print("\nAlex".lstrip()) # 从左边去掉换行与回车
print("Alex\n".rstrip()) # 从右边边去掉换行与回车
print("          Alex\n".strip()) # 从两边去掉换行与回车
p = str.maketrans("abcdefli","123@$456")

print("alex li".translate(p))

print("alex li".replace('i','L',1)) #替换，如果只想换一个count记1
print("alex li".rfind('l')) # 知道最右面的值
print("alex li".split()) # 按照空格分成列表
print("1+2+3+4".split("+")) # 根据加号把数字分成列表
print("1+2\n+3+4".splitlines()) #
print("Alex Li".swapcase()) #大小写转换
print("lex Li".title())
print("lex Li".zfill(50))