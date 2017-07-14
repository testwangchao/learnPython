#!/usr/bin/env python
#coding:utf-8
import random,string
'''
生成字符
'''
#方式一
def randomChar():
    #65~99是字母表[a-z]的ASCII值
    # 先获取随机的ASCII值，然后利用chr方法转换为单个的字母
    # 如果是[a-z, A-Z]，则数值范围为65~122
    random_char = chr(random.randint(65,122))
    print random_char
#方式二
def randomChar2():
    random_char=random.choice(string.ascii_letters)
    print random_char
'''
生成字符串
'''
#可重复字符串
def randomStr(length):
    print "".join(random.choice(string.ascii_letters) for i in range(length))
#不可重复字符串
def randomStr2(length):
    print "".join(random.sample(string.ascii_letters,length))
if __name__=="__main__":
    randomChar2()
    randomStr(5)
    randomStr2(3)