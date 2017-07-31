# Author:Da pan
import getpass,sys,os

i = 0
while i < 3:

    name = input("请输入用户名:")

    lock_file = open('account_lock.txt', 'r+')
    lock_list = lock_file.readlines()

    for lock_line in lock_list:
        # print(lock_line)
        if name == lock_line.strip():
            sys.exit("用户%s已经被锁定" % name)

    user_file = open("account.txt","r")
    user_list = user_file.readlines()
    for user_line in user_list:
        (user,passWord) = user_line.strip().split()
        if name == user:
            j = 0
            while j < 3:
                passwd = input("password:")
                if passwd == passWord:
                    print("登录成功 %s" %name)
                    sys.exit()
                else:
                    if j != 2:
                        print('用户 %s 密码错误，请重新输入，还有 %d 次机会' % (name, 2 - j))
                j += 1
            else:
                lock_file.write(name+"\n")
                sys.exit('用户 %s 达到最大登录次数，将被锁定并退出' % name)
    else:
        if i != 2:
            print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (name, 2 - i))
    i += 1
else:
    sys.exit('用户 [_name] 不存在，退出' .format(_name=name))

#关闭LOCK文件
lock_file.close()
user_file.close()





