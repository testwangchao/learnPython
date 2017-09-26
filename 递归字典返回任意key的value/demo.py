# coding:utf-8
def demo(test_data, key_data):
    if isinstance(test_data, dict):
        for key, value in test_data.items():
            if key == key_data:
                return value
            else:
                if isinstance(value, dict):
                    data = demo(value, key_data)
                    return data


def main():
    test = {"a": {"b": 7, "f": {"t": 8}}, "d": {"e": 1}}
    print demo(test, "t")


if __name__ == '__main__':
    main()