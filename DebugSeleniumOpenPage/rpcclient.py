# coding:utf-8

import pickle
class RPCProxy(object):

    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        # 通过name，得到一个函数
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc
def demo(driver):
    driver.get("http://www.baidu.com")
    print driver.find_element_by_id("kw").is_displayed()
# 远程连接并且调用
if __name__ == '__main__':

    from multiprocessing.connection import Client
    rpc_client = Client(('localhost', 17000), authkey='tab_space')

    proxy = RPCProxy(rpc_client)
    proxy.get()