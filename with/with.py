# coding:utf-8
'''
在进入上下文和离开上下文时，对象的text属性发生了改变(最初的text属性是"I'm fine")。
__enter__()返回一个对象。上下文管理器会使用这一对象作为as所指的变量，也就是myvow。在__enter__()中，
我们为myvow.text增加了前缀 ("I say: ")。在__exit__()中，我们为myvow.text增加了后缀("!
'''


class VOW(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "I say: " + self.text  # add prefix
        return self  # note: return an object

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "!"  # add suffix


with VOW("I'm fine") as myvow:
    print(myvow.text)
print myvow.text
