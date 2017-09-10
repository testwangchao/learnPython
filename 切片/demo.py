# coding:utf-8
list1 = [10,11,13,16,18]
print list1[:2]     # 在下标2的地方分割, [10, 11]
print list1[2:]     # 从下标2的地方开始分割，[13, 16, 18]
test_str = "Test_demo"
print test_str[:2:2]   # T
print test_str[::3]    # Tte
print test_str[::-2]   # oe_sT
# slice对象
a = slice(0,3)
print test_str[a]      # Tes
# 给切片赋值
list2 = [1,4,2,6,77]
list2[0:3]=[7777]
print list2     # [7777, 6, 77]
