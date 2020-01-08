from pages.login import LoginFun
from pages.shop import Shop
from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest

'''
    1   点击店铺查询按钮进入店铺查询界面
    2   点击发展商家，切换到发展商家页面
    3   点击进入已发展的商家，上传图片
    4   点击进入已发展的商家，对上传的图片进行删除
'''
class Shop_test(unittest.TestCase):
    '''店铺查询测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.s = Shop(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()
        self.s.click_cut()
        time.sleep(3)

    def test_shop_01(self):
        '''点击店铺查询按钮进入店铺查询界面'''
        loc = (By.XPATH,"//div[@class='bottomnav']/div/a[4]")
        t = self.s.get_rpg(loc)
        self.assertTrue(t,"#f86e23")

    def test_shop_02(self):
        '''点击发展商家，切换到发展商家页面'''
        self.s.click_progress_shop()
        t = self.s.get_pro_color()
        self.assertEqual(t,"#ff8724")

    def test_shop_03(self):
        '''点击进入已发展的商家，上传图片'''
        self.s.click_progress_shop()
        self.s.click_first_shop()
        self.s.sendkey_img()

    def test_shop_04(self):
        '''点击进入已发展的商家，对上传的图片进行删除'''
        self.s.click_progress_shop()
        self.s.click_first_shop()
        self.s.click_X()

    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
