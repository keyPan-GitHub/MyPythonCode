

import time


# print("start to sleep")
# time.sleep(3)
# print("week up")
# 时间戳
print(time.time())
# 输出当前系统时间
print(time.ctime(time.time()-86400))
time_obj = time.gmtime(time.time()-86400)
print(time_obj)
print(str(time_obj.tm_year)+ "-" + str(time_obj.tm_mon) + "-" + str(time_obj.tm_mday))

print("%d-%s-%s %s:%s" %(time_obj.tm_year, time_obj.tm_mon, time_obj.tm_mday, time_obj.tm_hour, time_obj.tm_min))
# 本地时间
print(time.localtime(time.time()+86400))
# 将时间对象，转回时间戳
print(time.mktime(time.localtime()))

# 将指定时间对象转换成字符串格式
# print(time.strftime("%Y-%m-%d %H:%M", time.localtime())

print(time.strptime("2017-08-18 12:43:30","%Y-%m-%d %H:%M:%S"))







