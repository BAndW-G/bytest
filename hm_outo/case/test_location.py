from pages.login import LoginFun
from pages.home import Home
from pages.location import Location
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest
import time

'''
    1   查看首页定位于当前定位地址是否一致
    2   正常切换地址，查看地址切换是否成功
    3   点击当前定位，定位切换为当前位置
'''

class Location_test(unittest.TestCase):
    '''定位界面测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.r = Location(cls.driver)
        cls.h = Home(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()
        self.r.click_orientation()

    def test_location_01(self):
        '''查看首页定位于当前定位地址是否一致'''
        t1 = self.h.get_orie_home_text()
        t2 = self.r.get_loca_text()
        print("测试数据 %s %s"%t1 %t2)
        self.assertTrue(t1,t2)

    def test_location_02(self):
        '''查看首页定位于当前定位地址是否一致'''
        self.r.click_switch_area()
        t1 = self.h.get_orie_home_text()
        print("测试数据 %s"%t1)
        self.assertTrue(t1,"天河区")

    def test_location_03(self):
        '''点击当前定位，定位切换为当前位置'''
        self.r.click_switch_area()
        self.r.click_orientation()
        time.sleep(2)
        t1 = self.r.get_loca_text()
        self.r.click_current_location()
        time.sleep(2)
        t2 = self.h.get_orie_home_text()
        self.assertTrue(t1,t2)

