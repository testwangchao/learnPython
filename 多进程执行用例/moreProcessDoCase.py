#coding:utf-8
from selenium import webdriver
import multiprocessing
import unittest
import time
driver = webdriver.Chrome()
class TestCase(unittest.TestCase):
    def test_openUrl1(self):
        print 'TestCase'
        driver.get("http://testadmin.yumimobi.com")
        #print time.ctime()
        self.assertEqual(1,22)
    def test_openUrl2(self):
        print 'TestCase'
        driver.get("http://testadmin2.yumimobi.com")
        driver.find_element_by_id('username').send_keys('wangchao@zplay.com')
        driver.find_element_by_id('password').send_keys('wang5688733')
class TestCase2(unittest.TestCase):
    def setUp(self):
        pass
    def test_openUrl1(self):
        print 'TestCase2'
        driver.get("http://testadmin.yumimobi.com")
        #print time.ctime()
        self.assertEqual(1,22)
    def test_openUrl2(self):
        print 'TestCase2'
        driver.get("http://testadmin2.yumimobi.com")
        driver.find_element_by_id('username').send_keys('wangchao@zplay.com')
        driver.find_element_by_id('password').send_keys('wang5688733')
        #print time.ctime()
        self.assertEqual(driver.title,'test')
#运行测试用例的集合
def run(func):
    print time.ctime()
    suite = unittest.TestLoader().loadTestsFromTestCase(func)
    unittest.TextTestRunner().run(suite)
    #runner.run(suite)
if __name__ == '__main__':
    print '----------------------------------'
    #使用进程池
    pool = multiprocessing.Pool(processes=2)
    for func in [TestCase,TestCase2]:
        pool.apply_async(run,(func,))
    print 'start!'
    #一个进程执行完成后关闭
    pool.close()
    #待上一个进行执行完成下一个进程进行
    pool.join()
    print 'other start!'


