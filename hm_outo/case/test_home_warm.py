from pages.login import LoginFun
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest
import time
'''
    1   点击温馨提示的关闭按钮，弹窗关闭
    2   点击温馨提示的去入驻按钮，跳转至入驻界面
    3   点击弹窗以外任意位置，弹窗关闭
'''
class Warm_test(unittest.TestCase):
    '''首页弹窗测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()

    def loginx(self):
        self.l.input_user()
        self.l.input_pwd()
        self.l.click_login_button()

    def test_warm_01(self):
        '''点击温馨提示的关闭按钮'''
        self.loginx()
        self.l.close_home_warm()
        time.sleep(2)
        #t = self.driver.find_element_by_xpath("//div[@class='mint-msgbox-wrapper']/div").get_attribute("style")
        loc = (By.XPATH,"//div[@class='mint-msgbox-wrapper']/div")
        t = self.l.get_att(loc,"style")
        print (t)
        self.assertTrue(t == "display: none;")

    def test_warm_02(self):
        '''点击温馨提示的去入驻按钮'''
        self.loginx()
        loca = (By.XPATH,"//div[@class='mint-msgbox-btns']/button[2]")
        self.l.clk(loca)
        #   now_url = self.driver.current_url 获取当前界面URL
        loc = (By.XPATH,"//h1[@class='mint-header-title']")
        t = self.l.rtext(loc)
        print(t)
        self.assertTrue(t == "上传信息")

    def test_warm_03(self):
        '''点击弹窗以外任意位置'''
        self.loginx()
        time.sleep(2)
        self.l.locxy_click(self.driver,10,10)
        time.sleep(2)
        #t = self.driver.find_element_by_xpath("//div[@class='mint-msgbox-wrapper']/div").get_attribute("style")
        loc = (By.XPATH,"//div[@class='mint-msgbox-wrapper']/div")
        t = self.l.get_att(loc,"style")
        print (t)
        self.assertTrue(t == "display: none;")

    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__mian":
    unittest.main()