from pages.login import LoginFun
from pages.home import Home
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest
import time
'''
    1   点击首页banner图，界面跳转至消费券专区
    2   点击当前位置，跳转到切换地址页面
    3   点击搜索框，跳转到搜索界面
    4   点击私信按钮，跳转到消息中心
    5   当前所在位置有无惠盟商家，无商家时，界面显示广告图片
    6   存在未支付订单提示，点击去支付，跳转到订单界面
    7   拖动导航列表，查看导航列表是否换页
'''


class Home_skip_test(unittest.TestCase):
    '''首页跳转测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.h = Home(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()

    def test_home_01(self):
        '''点击首页banner图，界面跳转至消费券专区'''
        self.h.click_banner()
        t = self.h.get_voucher()
        print("测试数据 %s"%t)
        self.assertTrue(t,"百业惠盟消费劵专区")

    def test_home_02(self):
        '''点击当前位置，界面跳转到切换地址页面'''
        self.h.click_orientation()
        time.sleep(2)
        t = self.h.get_orien_text()
        print("测试数据 %s"%t)
        self.assertTrue(t,"选择地址")

    def test_home_03(self):
        '''点击搜索框，跳转到搜索界面'''
        self.h.click_home_input()
        t = self.h.get_input_text()
        print("测试数据 %s"%t)
        self.assertTrue(t,"搜索")

    def test_home_04(self):
        '''点击私信按钮，跳转到消息中心'''
        self.h.click_private_letter()
        time.sleep(2)
        t = self.h.get_letter_text()
        print("测试数据 %s"%t)
        self.assertTrue(t,"消息中心")

    def test_home_05(self):
        '''当前所在位置有无惠盟商家，无商家时，界面显示广告图片'''
        t = self.h.is_displayed_ad()
        if t == True:
            print("无商家 %s"%t)
            self.assertTrue(t,True)
            d = self.h.is_displayed_cp()
            self.assertTrue(d,False)
        else:
            print("有商家 %s"%t)
            self.assertTrue(t,False)
            d = self.h.is_displayed_cp()
            self.assertTrue(d,True)

    def test_home_06(self):
        '''存在未支付订单提示，点击去支付，跳转到订单界面'''
        self.h.click_prompt_order()
        t = self.h.get_order_text()
        print("测试数据: %s"%t)
        self.assertTrue(t,"我的订单")

    def test_home_07(self):
        '''拖动导航列表，查看导航列表是否换页'''
        t = self.h.get_color_value()
        self.assertTrue(t,"#4cdb6a")

    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
