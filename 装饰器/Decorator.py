#coding:utf-8
'''
python中装饰器的基本用法
'''
import logging,unittest
from functools import wraps

'''
#装饰器函数
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         logging.debug("start deco")
         print 'Calling decorated function'
         return f()
         logging.info("strat end")
     return wrapper
@my_decorator
def f():
    print 'test!'
f()
'''


class Sum():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
#类中使用装饰器
class deco():
    def __call__(self,func):
        @wraps(func)
        def write(self,*args,**kwargs):
            logging.basicConfig(level=logging.INFO)
            logging.info(func.__name__)
            return func(self)  #在其它类中使用装饰器类时，需要在此处加入self，self在这仅充当一个参数
        return write

class TestSum(unittest.TestCase):
    @deco()
    def test_sum1(self):
        self.assertEqual(Sum(2,3).add(),6)

if __name__ == "__main__":
    unittest.main()



