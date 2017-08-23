

import datetime,time


print(datetime.date.today())  #输出可是 2016-10-1 
#输出可是 2016-10-1 将时间错转换成日期格式
print(datetime.date.fromtimestamp(time.time()-86400))   

current_time = datetime.datetime.now()
print(current_time) #输出当前时间
print(current_time.timetuple()) # 返回时间对象（struct——time）
# 时间替换
print(current_time.replace(2014,10,10,11,20))
print(current_time.replace())

# 从现在+ 10天
print(datetime.datetime.now() + datetime.timedelta(days=10))
print(datetime.datetime.now() + datetime.timedelta(hours=-10))
print(datetime.datetime.now() + datetime.timedelta(seconds=10000))
print(datetime.datetime.now() + datetime.timedelta(weeks=1))















