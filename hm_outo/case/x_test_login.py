#coding=utf-8
import time
import unittest
from selenium import webdriver
from pages.login import LoginFun


class Login_test(unittest.TestCase):
    '''登录类测试'''

    @classmethod
    def setUpClass(cls):
        #打开浏览器
        cls.driver = webdriver.Chrome()
        #实例化 LoginFun
        cls.logfun = LoginFun(cls.driver)


    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://byhm.520shq.com/#/login')
        self.driver.maximize_window()

    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    def test_login01(self):
        '''正确用户名密码'''
        #登录
        self.logfun.login()
        #time.sleep(2)
        t = self.logfun.get_login_sucess()
        print("获取结果：%s"%t)
        #判断是否有登录成功的提示
        #unittest自带 assert 断言
        self.assertTrue(t == "登录成功")

    def test_login02(self):
        '''错误用户名密码'''
        #登录
        self.logfun.login(user="13600001234",pwd="321654")
        #time.sleep(2)
        t = self.logfun.get_login_sucess()
        print("获取结果:%s"%t)
        # 判断是否有登录成功的提示
        # unittest自带 assert 断言
        self.assertTrue(t == "用户不存在或密码错误")
