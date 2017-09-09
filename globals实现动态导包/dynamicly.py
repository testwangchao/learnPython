#coding:utf-8
import importlib
#globals()检测全局变量
para1 = 2
para2 = 'test'
para3 = {'key':'value'}
def learnGlobal():
    print globals()
    #out返回类型为dict
    #{'learnGlobal': <function learnGlobal at 0x025CA4B0>, 'importlib': <module 'importlib' from 'C:\Python27\lib\importlib\__init__.pyc'>,'__builtins__': <module '__builtin__' (built-in)>, '__file__': 'E:/learnPython/globals\xca\xb5\xcf\xd6\xb6\xaf\xcc\xac\xb5\xbc\xb0\xfc/dynamicly.py', '__package__': None, 'para3': {'key': 'value'}, 'para2': 'test', 'para1': 2, '__name__': '__main__', '__doc__': None}
#locals()检测局部变量
def learnLocal():
    var = 1
    para3 = {'key':'value'}
    print locals()
    #out返回类型为dict
    #{'var': 1}
#动态导包
def dymamic(modelName):
    for model in modelName:
        globals()[model]=importlib.import_module(model)
        print globals()
if __name__ == '__main__':
    #learnGlobal()
    #learnLocal()
    dymamic(['requests','unittest'])
    print requests.get("http://www.baidu.com").content
