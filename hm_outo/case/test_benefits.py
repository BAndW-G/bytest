from pages.login import LoginFun
from pages.benefits import Benefits
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest
import time

'''
    1   点击用户福利按钮进入用户福利界面，通过按钮颜色变化判断是否进入用户福利界面
    2   点击订单按钮,进入订单界面
    3   在订单界面点击返回按钮，返回用户福利界面
    4   点击续费按钮,进入续费界面,判断会员卡类型和金额
    5   在续费点击返回按钮，返回用户福利界面
    6   在续卡界面点击立即购买，界面跳转到确认订单界面
    7   立即购买按钮，点击前可用点击，点击按钮变化灰色
    8   点击消费券详情，进入消费券详情页
    9   判断已获赠的数量是否与显示出的获赠次数是否相等
    10  判断已送出的数量是否与显示出的送出次数是否相等
    11  判断消费券余额显示是否等于累计减去已使用
    12  点击去使用，跳转至惠盟专区
'''

class Benefits_test(unittest.TestCase):
    '''用户福利测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.b = Benefits(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()
        self.b.click_cut()
        time.sleep(3)

    def test_benefits_01(self):
        '''点击用户福利按钮进入用户福利界面'''
        loc = (By.XPATH,"//div[@class='bottomnav']/div/a[3]")
        t = self.b.get_rpg(loc)
        self.assertTrue(t,"#f86e23")

    def test_benefits_02(self):
        '''点击订单按钮进入订单界面'''
        self.b.click_order()
        ele = (By.CSS_SELECTOR,"div.top_nav>span")
        t = self.b.rtext(ele)
        self.assertEqual(t,"我的订单")

    def test_benefits_03(self):
        '''在订单界面点击返回按钮，返回用户福利界面'''
        self.b.click_order()
        self.b.click_return()
        loc = (By.XPATH,"//h1")
        t = self.b.get_rpg(loc)
        self.assertTrue(t,"惠盟用户福利")

    def test_benefits_04(self):
        '''点击续费按钮,进入续费界面'''
        self.b.click_renew()
        ele1 = (By.XPATH,"//h1")
        ele2 = (By.CSS_SELECTOR,"div.card-title")
        ele3 = (By.CSS_SELECTOR,"div.card-price")
        t1 = self.b.rtext(ele1)
        self.assertEqual(t1,"续卡")
        t2 = self.b.rtext(ele2)
        self.assertEqual(t2,"会员年卡")
        t3 = self.b.rtext(ele3)
        self.assertEqual(t3,"¥ 365.00")

    def test_benefits_05(self):
        '''在订单界面点击返回按钮，返回用户福利界面'''
        self.b.click_renew()
        self.b.click_renew_return()
        loc = (By.XPATH,"//h1")
        t = self.b.get_rpg(loc)
        self.assertTrue(t,"惠盟用户福利")

    def test_benefits_06(self):
        '''在续卡界面点击立即购买，界面跳转到确认订单界面'''
        self.b.click_renew()
        self.b.click_renew_buy()
        loc = (By.XPATH,"//h1")
        t = self.b.get_rpg(loc)
        self.assertTrue(t,"确认订单")

    def test_benefits_07(self):
        '''立即购买按钮，点击前可用点击，点击按钮变化灰色'''
        self.b.click_renew()
        t1 = self.b.enabled_renew_buy()
        self.assertTrue(t1)
        self.b.click_renew_buy()
        ele = (By.CSS_SELECTOR,"div.pay-btn")
        t2 = self.b.get_back_rpg(ele)
        self.assertEqual(t2,"#999999")

    def test_benefits_08(self):
        '''点击消费券详情，进入消费券详情页'''
        self.b.click_cards_particulars()
        time.sleep(2)
        ele = (By.XPATH,"//h1")
        t = self.b.rtext(ele)
        self.assertEqual(t,"消费劵详情")

    def test_benefits_09(self):
        '''判断已获赠的数量是否与显示出的获赠次数是否相等'''
        self.b.click_cards_particulars()
        self.b.click_gain_cards()
        t1 = self.b.get_num()
        t2 = self.b.get_list_total()
        self.assertEqual(t1,str(t2))

    def test_benefits_10(self):
        '''判断已送出的数量是否与显示出的送出次数是否相等'''
        self.b.click_cards_particulars()
        self.b.click_senk_cards()
        t1 = self.b.get_num()
        t2 = self.b.get_list_total()
        self.assertEqual(t1,str(t2))

    def test_benefits_11(self):
        '''判断消费券余额显示是否等于累计减去已使用'''
        self.b.click_cards_particulars()
        f1 = self.b.get_addUp_text()
        f2 = self.b.get_use_text()
        f3 = self.b.get_balance_text()
        f4 = f1-f2
        self.assertEqual(f3,f4)

    def test_benefits_12(self):
        '''点击去使用，跳转至惠盟专区'''
        self.b.click_cards_particulars()
        self.b.click_cards_use()
        ele = (By.XPATH,"//h1")
        t = self.b.rtext(ele)
        self.assertEqual(t,"百业惠盟消费劵专区")

    def test_benefits_13(self):
        '''点击转增，跳转至转增消费券界面'''
        self.b.click_cards_particulars()
        self.b.click_cards_donation()
        ele = (By.XPATH,"//h1")
        t = self.b.rtext(ele)
        self.assertEqual(t,"转增消费券")

    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

