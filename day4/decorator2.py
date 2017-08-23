# Author:Da pan

import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return deco


@timer  # dome1 = timer(dome1)
def dome1():
    time.sleep(3)
    print('in the dome1')


@timer
def dome2(name):
    # time.sleep(3)
    print('in the name', name)


dome1()
dome2("pipi")

# deco(dome1)
# deco(dome2)
# dome1=timer(dome1)
# dome1()
# print(timer(dome1))

# dome1()
# dome2()
