#coding:utf-8
from selenium import webdriver

class SingletonMode(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(SingletonMode,cls).__new__(cls,*args,**kwargs)
            global driver
            driver = SingletonMode().Getdriver()
        return cls._instance
    def Getdriver(self):
        return webdriver.Chrome()
    def add(self):
        return driver


a = SingletonMode()
b = SingletonMode()
print a
print b
a.add().get("http://www.baidu.com")
a.add().get("http://www.taobao.com")