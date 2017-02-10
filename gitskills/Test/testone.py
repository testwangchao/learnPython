#coding:utf-8
import unittest
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class AppAudit(unittest.TestCase):
    def setUp(self):
        pass
    def testUser(self):
        OpenBrowser = webdriver.Remote(command_executor="http://testwangchao:1b7cab22-028e-4940-a1bf-f1af92292ce1@ondemand.saucelabs.com:80/wd/hub",
                                       desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        OpenBrowser.get('http://testadmin.yumimobi.com/index.php/user/login?t=ff3dcb761ba35ff0081d719aec691f58c4')
        locatorA = (By.XPATH,".//*[@id='sidebar']/div/div[1]/div")
        locatorB = (By.LINK_TEXT,u"账号审核")
        locatorC = (By.XPATH,".//*[@id='search']/div[3]/div/div[1]/p")
        locatorD = (By.XPATH,".//*[@id='search']/div[3]/div/div[2]/div[3]")
        try:
            WebDriverWait(OpenBrowser,10,0.5).until(EC.presence_of_element_located(locatorA))
            OpenBrowser.find_element_by_xpath(".//*[@id='sidebar']/div/div[1]/div").click()
            sleep(0.5)
            WebDriverWait(OpenBrowser,10,0.5).until(EC.presence_of_element_located(locatorB))
            OpenBrowser.find_element_by_link_text('账号审核').click()
            sleep(0.5)
            WebDriverWait(OpenBrowser,10,0.5).until(EC.presence_of_element_located(locatorC))
            OpenBrowser.find_element_by_xpath(".//*[@id='search']/div[3]/div/div[1]/p").click()
            sleep(0.5)
            WebDriverWait(OpenBrowser,10,0.5).until(EC.presence_of_element_located(locatorD))
            OpenBrowser.find_element_by_xpath(".//*[@id='search']/div[3]/div/div[2]/div[3]").click()
        finally:
            testSoup=BeautifulSoup(OpenBrowser.page_source,'html.parser')
            self.assertEqual(testSoup.find(class_="j_cell cell cell2",string='中国').string,u'中国')
            self.assertEqual(testSoup.find(class_="j_cell cell cell3",string='iOS').string,'iOS')
            self.assertEqual(testSoup.find(class_="j_cell cell cell4",string='审核通过').string,u'审核1通过')
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()