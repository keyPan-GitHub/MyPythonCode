# 开放封闭原则


def outer(func):
    def inner():
        print("hello")
        print("hello")
        print("hello")
        r = func()  # r = None
        print("end")
        print("end")
        print("end")
        return r

    return inner


@outer
def f1():
    print("F1")


# 装饰器目的：
# 在不改变原函数代码，不改变原函数调用方式的前提情况下，让它在执行原函数之前或之后，做点什么操作
# 只要函数应用装饰器，那么函数就将被重新定义，重新定义为：装饰器的内层函数
# @outer
# 1、执行outer函数，将index作为参数传递
# 2、将outer的返回值，重新赋值给index

# 1、执行outer函数，并将其下面的f1函数名，当作参数
# 2、将outer的返回值重新赋值给f1  所以f1等于 outer的返回值
# 3、新f1函数 = inner
ret = f1()
print(ret)


def f2():
    print("F2")


def f3():
    print("F3")


def f4():
    print("F4")


def f100():
    print("F100")

# f1()
