# coding:utf-8
from collections import namedtuple

Demo = namedtuple("Demo", ("name", "age", "country"))      #只接受单一的可迭代对象
test_tuple = Demo("wangchao", "18", "China")
print test_tuple      # Demo(name='wangchao', age='18', country='China')
print test_tuple.name   # wangchao
# test_tuple.name = "ds"      # 会报错，元组不能进行改变
print test_tuple._replace(name = "test")    #　Demo(name='test', age='18', country='China')，但是test_tuple本身不发生变化
print test_tuple[0]     # wangchao