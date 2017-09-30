# coding:utf-8
'''
python中装饰器的基本用法
'''
import logging
import unittest
from functools import wraps
import logging

logging.basicConfig(level="INFO")

# 装饰器函数
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        logging.debug("start deco")
        print 'Calling decorated function'
        func(*args)
        logging.info("strat end")

    return wrapper


@my_decorator  # 等价于f = my_decorator(f)    f()
def f(msg):
    print msg


class Sum():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


# 类中使用装饰器
class deco():
    def __call__(self, func):
        @wraps(func)
        def write(self, *args, **kwargs):
            logging.basicConfig(level=logging.INFO)
            logging.info(func.__name__)
            return func(self)  # 在其它类中使用装饰器类时，需要在此处加入self，self在这仅充当一个参数

        return write


class TestSum(unittest.TestCase):
    @deco()
    def test_sum1(self):
        self.assertEqual(Sum(2, 3).add(), 6)


# 带参数的装饰器
'''
相当于：
test_func = write_log("test_func")(test_func)
test_func()
'''


def write_log(msg):
    def decorator(func):
        @wraps(func)
        def inner():
            func()
            logging.info(msg)

        return inner

    return decorator


@write_log("This is test.")
def test_func():
    print "test"


# 将装饰器定义为类的一部分
class Demo(object):
    def __init__(self):
        super(Demo, self).__init__()

    def deco(self, func):
        @wraps(func)
        def inner(*args):
            print "test"
            func(*args)

        return inner


a = Demo()


@a.deco
def test_demo():
    print "test_demo"


if __name__ == "__main__":
    f("test")
