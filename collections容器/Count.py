# coding:utf-8
'''
一、Counter类的创建（iterable对象创建）
   Counter("sadsadsa")、Counter([1,2,3,1,2])、Counter((1,23,555,1,1))

'''
from collections import Counter
from collections import namedtuple
test_list = ["test1","test2","test3","test2"]
list_count = Counter(test_list)
print list_count["test2"]
print "------------------"
test_str = "aaabbbcfcjas"
dict_count = Counter(test_str)
print dict_count["b"]
print "------------------"
print list(dict_count.elements())
print "=================="
dict_count.update("abc")
print dict_count["b"]
test1 = Counter(a=1,b=2)
print test1['b']
print list_count
print "////////////////////"
Demo = namedtuple("Demo",['x','y'])
test_demo = (1,2)
a = Demo._make(test_demo)
b = a._asdict()
print b.get("x")
