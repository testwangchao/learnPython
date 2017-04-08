#coding:utf-8
class Property(object):
    def __init__(self):
        self.test = 'test1'
    #获取属性
    @property
    def TestProperty(self):
        return self.test
    #设置属性
    @TestProperty.setter
    def TestProperty(self,value):
        self.test = value
    #删除属性
    @TestProperty.deleter
    def TestProperty(self):
        del self.test
a = Property()
#将类方法变成了属性，可以直接调用，不需要括号
print a.TestProperty
#可以设置属性
a.TestProperty = "test2!"
print a.TestProperty
print 1111111111
del a.TestProperty
a.TestProperty = "test2!"
print a.TestProperty
