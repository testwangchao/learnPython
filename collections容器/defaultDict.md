#### defaultdict
1. defaultdict：通过使用一个类型名称或为空进行初始化
```
from collections import defaultdict
# 可以初始化列表、字典、集合等类型
test_type = [defaultdict(i) for i in [list,dict]]
print test_type
```
输出：[defaultdict(<type 'list'>, {}), defaultdict(<type 'dict'>, {})]
2. 当访问的键不存在时，可以实例化一个值作为默认值
```
test_list = defaultdict(list)
print test_list.get("key1")
```
输出：None


```
# 初始化list
test_list = defaultdict(list)
# 默认值为空
default_value = test_list["key1"]
test_list["key2"] = 5
for key in ["key1", "key2"]:
    print test_list.get(key)
```
输出：[] 5
