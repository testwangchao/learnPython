# coding:utf-8
from SimpleXMLRPCServer import SimpleXMLRPCServer
from selenium.webdriver.chrome.webdriver import WebDriver
import client
# 驱动地址
driver = WebDriver(executable_path="chromedriver.exe")


def get():
    reload(client)
    client.demo(driver)


if __name__ == "__main__":
    s = SimpleXMLRPCServer(("localhost", 8080), allow_none=True)
    s.register_function(get)
    s.serve_forever()
