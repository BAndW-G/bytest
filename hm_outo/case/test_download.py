from pages.login import LoginFun
from common.simulation import simu_driver
from selenium.webdriver.common.by import By
from pages.home import Home
import unittest
'''
    1   点击下载按钮，跳转到下载界面  (暂时无法完成）
    2   点击关闭按钮，下载提示关闭
'''
class Download_Test(unittest.TestCase):
    '''下载提示测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.h = Home(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()

    def test_download_02(self):
        '''删除下载提示'''
        #   无法断言
        loc_x = (By.XPATH,"//div[@class='guide']/div/i")
        self.h.click_x()

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


