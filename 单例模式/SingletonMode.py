#coding:utf-8
from selenium import webdriver

class SingletonMode(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(SingletonMode,cls).__new__(cls,*args,**kwargs)
            #global driver
            #driver = SingletonMode().Getdriver()
        return cls._instance
    @staticmethod
    def Getdriver():
        return webdriver.Chrome()

class Add(SingletonMode):
    #global driver
    driver = SingletonMode.Getdriver()
    def get(self):
        return self.driver

a = Add()
b = Add()
print a
print b
a.get().get("http://www.baidu.com")
a.get().get("http://www.taobao.com")