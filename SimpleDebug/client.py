# coding:utf-8
from xmlrpclib import ServerProxy
from time import sleep


# 调试元素的方法
def demo(driver):
    driver.get("http://www.baidu.com")
    # driver.maximize_window()
    sleep(0.2)


if __name__ == "__main__":
    s = ServerProxy("http://127.0.0.1:8080", allow_none=True)
    s.get()
