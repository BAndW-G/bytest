from pages.login import LoginFun
from pages.shop import Homeshop
from pages.location import Location
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest
import time

'''
    1   点击商家图片，进入商家详情页
    2   点击商家信息其他元素，可以进入商家详情页
    3   点击更多按钮，会有信息栏弹出，再次点击，信息栏关闭
    4   点击更多按钮中的用户福利按钮，界面跳转到用户福利界面
    5   点击更多按钮中分享按钮，提示在微信浏览器中分享
    6   点击图片按钮，进入全部图片界面
    7   点击导航按钮，进入到导航界面
    8   点击店铺优惠，按钮变色，界面下拉到优惠处
    9   点击环境，按钮变色，界面下拉到环境图片处
    10  点击商家信息，按钮变色，界面下拉到商家信息处
'''


class Home_skip_test(unittest.TestCase):
    '''首页商家测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.s = Homeshop(cls.driver)
        cls.r = Location(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()
        self.r.click_orientation()
        self.r.click_switch_area()
        time.sleep(3)

    def test_skip_01(self):
        '''点击商家图片，可以进入商家详情页'''
        self.s.click_img_shop()
        t = self.s.get_shop_text()
        self.assertTrue(t,"店铺详情")

    def test_skip_02(self):
        '''点击商家信息其他元素，可以进入商家详情页'''
        self.s.click_ele_shop()
        t = self.s.get_shop_text()
        self.assertTrue(t,"店铺详情")

    def test_skip_03(self):
        '''点击更多按钮，会有信息栏弹出，再次点击，信息栏关闭'''
        self.s.click_img_shop()
        self.s.click_more()
        t = self.s.display()
        self.assertTrue(t,True)
        self.s.click_more()
        t = self.s.display()
        self.assertFalse(t,False)

    def test_skip_04(self):
        '''点击更多按钮中的用户福利按钮，界面跳转到用户福利界面'''
        self.s.click_img_shop()
        time.sleep(2)
        self.s.click_benefits()
        loc = (By.XPATH,"//div[@class='bottomnav']/div/a[3]")
        t = self.s.get_rpg(loc)
        self.assertTrue(t,"#f86e23")

    def test_skip_05(self):
        '''点击更多按钮中分享按钮，提示在微信浏览器中分享'''
        self.s.click_img_shop()
        time.sleep(2)
        self.s.click_share()
        t = self.s.get_share_text()
        self.assertEqual(t,"请在微信浏览器中分享")

    def test_skip_06(self):
        '''点击图片按钮，进入全部图片界面'''
        self.s.click_img_shop()
        self.s.click_look_img()
        loc = (By.CSS_SELECTOR,"div.official")
        t = self.s.is_displayed_ele(loc)
        self.assertTrue(t,True)

    def test_skip_07(self):
        '''点击导航按钮，进入到导航界面'''
        self.s.click_img_shop()
        self.s.click_navigation()
        t = self.s.get_navigation_text()
        self.assertEqual(t,"地图显示")

    def test_skip_08(self):
        '''点击店铺优惠，按钮变色，界面下拉到优惠处'''
        self.s.click_img_shop()
        time.sleep(2)
        self.s.cilck_discount_stores()
        t1 = self.s.get_discount_class()
        self.assertEqual(t1,"hover")
        t2 = self.s.get_surroundings_class()
        self.assertEqual(t2,"")
        t3 = self.s.get_information_class()
        self.assertEqual(t3,"")

    def test_skip_09(self):
        '''点击环境，按钮变色，界面下拉到环境图片处'''
        self.s.click_img_shop()
        time.sleep(2)
        self.s.cilck_discount_stores()
        t1 = self.s.get_discount_class()
        self.assertEqual(t1,"")
        t2 = self.s.get_surroundings_class()
        self.assertEqual(t2,"hover")
        t3 = self.s.get_information_class()
        self.assertEqual(t3,"")

    def test_skip_10(self):
        '''点击商家信息，按钮变色，界面下拉到商家信息处'''
        self.s.click_img_shop()
        time.sleep(2)
        self.s.cilck_discount_stores()
        t1 = self.s.get_discount_class()
        self.assertEqual(t1,"")
        t2 = self.s.get_surroundings_class()
        self.assertEqual(t2,"")
        t3 = self.s.get_information_class()
        self.assertEqual(t3,"hover")

    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()






















