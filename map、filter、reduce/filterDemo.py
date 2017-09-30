# coding:utf-8
import types


def func():
    return "test"

# 过滤函数
def is_function(name):
    # return isinstance(name, types.FunctionType)
    return name %2 == 0

def filter_demo(func_name, data):
    return [i for i in data if func_name(i) is True]
    # for i in data:
    #     if func_name(i) is True:
    #         data_list.append(i)

if __name__ == '__main__':
    # a = filter(is_function, range(10))
    # print a
    a = lambda b: [i for i in b[1] if b[0](i) is True]