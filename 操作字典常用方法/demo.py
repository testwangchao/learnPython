# coding:utf-8

# 返回任意key的值
def demo(test_data, key_data):
    if isinstance(test_data, dict):
        for key, value in test_data.items():
            if key == key_data:
                return value
            else:
                if isinstance(value, dict):
                    data = demo(value, key_data)
                    return data
def demo_main():
    test = {"a": {"b": 7, "f": {"t": 8}}, "d": {"e": 1}}
    print demo(test, "t")

#　修改字典key的value
def update_dict(test_dict, update_key, update_value):
    for key, value in test_dict.items():
        if key == update_key:
            test_dict[key] = update_value
        else:
            if isinstance(value, dict):
                return update_dict(value, update_key, update_value)

def update_dict_main():
    test_dict = {"a": {"b": {"c": 1}}}
    update_dict(test_dict, "a", 2)
    print test_dict
if __name__ == '__main__':
    update_dict_main()