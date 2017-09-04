# coding:utf-8
from multiprocessing.connection import Listener
from threading import Thread
from selenium.webdriver.chrome.webdriver import WebDriver
import rpcclient
from rpcclient import demo
def rpc_server(handler, address, authkey):

    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args = (client,))
        t.daemon = True
        t.start()
if __name__=="__main__":
    driver = WebDriver(executable_path="H:\Corn_Selenium_Test\chromedriver.exe")
    def get():
        reload(rpcclient)
        rpcclient.demo(driver)
    from rpchandler import RPCHandler

    rpc_handler = RPCHandler()
    rpc_handler.register_function(get)

    # 运行server
    rpc_server(rpc_handler, ('localhost', 17000), authkey='tab_space')