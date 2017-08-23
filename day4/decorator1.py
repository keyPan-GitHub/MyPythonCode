# Author:Da pan
import time


def foo():
    print("in the foo")

    def bar():
        print("in the bar")

    bar()


foo()
