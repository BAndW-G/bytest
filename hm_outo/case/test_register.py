from selenium import webdriver
from pages.login import LoginFun
from pages.register import Register
from common.simulation import simu_driver
import unittest
'''
    1   不输入手机号，点击获取验证码按钮,提示手机号码格式错误
    2   仅点击注册按钮，提示用户暂不允许自主入住
    3   点击立即登录，返回登录界面
'''
class Register_Test(unittest.TestCase):
    '''注册页面测试'''

    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.r = Register(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        #   跳转注册界面
        self.l.click_registered()

    def test_register_01(self):
        '''不输入手机号，点击获取验证码按钮'''
        self.r.click_vc()
        t = self.driver.find_element_by_xpath("//span[@class='mint-toast-text']").text
        print("获取结果： %s"%t)
        #   断言
        self.assertTrue(t == "输入的手机号码格式错误！")

    def test_register_02(self):
        '''仅点击注册按钮'''
        self.r.click_button()
        t = self.driver.find_element_by_xpath("//span[@class='mint-toast-text']").text
        print("获取结果： %s"%t)
        #   断言
        self.assertTrue(t == "抱歉，百业惠盟暂不允许用户自行注册，需要有推荐人分享或者扫码推荐人二维码才能注册，请联系当地区域运营商分享链接或二维码进行注册，若有疑问可致电400-180-2520咨询。谢谢!")

    def test_register_03(self):
        '''点击立即登录，返回登录界面'''
        self.r.click_back_login()
        t = self.driver.find_element_by_css_selector(".sub").text
        print("获取结果： %s"%t)
        self.assertTrue(t == "登录")

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

