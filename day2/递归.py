# Author:Da pan


def calc(n):
    print(n)
    if int(n/2) == 0:
        return n
    return calc(int(n/2))

calc(10)


