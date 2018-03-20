# coding:utf-8

# 返回任意key的值
import json
import requests

def demo(test_data, key_data,delimiter='.'):
    for key in key_data.split(delimiter):
        if isinstance(test_data, dict):
            test_data = test_data.get(key)
        elif isinstance(test_data, list):
            return test_data[int(key)]
    return test_data
def demo_main():
    test = {"a": {"b": 7, "f": {"t": 8}}, "d": {"e": [5]}}
    print demo(test, "d.e.0")

#　修改字典key的value/
def update_dict(test_dict, update_key, update_value):
    for key, value in test_dict.items():
        if key == update_key:
            test_dict[key] = update_value
        else:
            if isinstance(value, dict):
                return update_dict(value, update_key, update_value)

if __name__ == '__main__':
    demo_main()
