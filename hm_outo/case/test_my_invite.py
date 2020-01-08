from pages.login import LoginFun
from pages.my import My
from selenium import webdriver
from pages.userLevel import Userlevel
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.by import By
from common.simulation import simu_driver
import unittest



'''
    1   显示出的邀请链接等级与运营商用户等级是否一致
    2   点击vip邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开
'''
class Invite(unittest.TestCase):
    '''邀请用户注册测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = simu_driver()
        cls.l = LoginFun(cls.driver)
        cls.m = My(cls.driver)
        cls.u = Userlevel(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()
        self.l.login()
        self.m.click_cut()

    def test_invite_01(self):
        '''显示出的邀请链接等级与运营商用户等级是否一致'''
        locli = (By.XPATH,"//div[@class='peopleClass inviteImg']//li//p")
        t = self.u.ulevel()
        s = self.m.rtext(locli)
        print(s)
        self.assertEqual(t,s)

    def test_invite_02(self):
        '''点击vip邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开'''
        self.m.js_scrollTop("2000")
        self.m.click_inviteImg06()
        self.m.click_copyUrl()
        url = self.m.get_url()
        #   获取当前浏览器的句柄
        window_1 = self.driver.current_window_handle
        print(window_1)
        #   用火狐浏览器打开链接
        self.driver2 = webdriver.Firefox()
        self.driver2.get(url)
        self.l2 = LoginFun(self.driver2)
        self.m2 = My(self.driver2)
        #   获取全部浏览器句柄，在进行判断，判断与之前的浏览器句柄是否一致，如果不一致切换到该浏览器窗口
        windows = self.driver2.window_handles
        print(windows)
        for current_window in windows:
            if current_window != window_1:
                self.driver2.switch_to.window(current_window)
        time.sleep(5)
        #   获取当前浏览器URL
        newurl = self.driver2.current_url
        print(newurl)
        self.assertEqual(newurl,"http://byhm.520shq.com/#/login")
        #   对第二个界面进行操作
        loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
        self.m2.is_displayed_ele(loc_user)
        self.l2.loginy("13600008888","a12345")
        self.driver.switch_to.window(window_1)

    def test_invite_03(self):
        '''点击推广大使邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开'''
        self.m.js_scrollTop("2000")
        self.m.click_inviteImg05()
        self.m.click_copyUrl()
        url = self.m.get_url()
        #   获取当前浏览器的句柄
        window_1 = self.driver.current_window_handle
        print(window_1)
        #   用火狐浏览器打开链接
        self.driver2 = webdriver.Firefox()
        self.driver2.get(url)
        self.l2 = LoginFun(self.driver2)
        self.m2 = My(self.driver2)
        #   获取全部浏览器句柄，在进行判断，判断与之前的浏览器句柄是否一致，如果不一致切换到该浏览器窗口
        windows = self.driver2.window_handles
        print(windows)
        for current_window in windows:
            if current_window != window_1:
                self.driver2.switch_to.window(current_window)
        time.sleep(5)
        #   获取当前浏览器URL
        newurl = self.driver2.current_url
        print(newurl)
        self.assertEqual(newurl,"http://byhm.520shq.com/#/login")
        #   对第二个界面进行操作
        loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
        self.m2.is_displayed_ele(loc_user)
        self.l2.loginy("13600008888","a12345")
        self.driver.switch_to.window(window_1)

    def test_invite_04(self):
        '''点击运营商邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开'''
        self.m.js_scrollTop("2000")
        self.m.click_inviteImg04()
        self.m.click_copyUrl()
        url = self.m.get_url()
        #   获取当前浏览器的句柄
        window_1 = self.driver.current_window_handle
        print(window_1)
        #   用火狐浏览器打开链接
        self.driver2 = webdriver.Firefox()
        self.driver2.get(url)
        self.l2 = LoginFun(self.driver2)
        self.m2 = My(self.driver2)
        #   获取全部浏览器句柄，在进行判断，判断与之前的浏览器句柄是否一致，如果不一致切换到该浏览器窗口
        windows = self.driver2.window_handles
        print(windows)
        for current_window in windows:
            if current_window != window_1:
                self.driver2.switch_to.window(current_window)
        time.sleep(5)
        #   获取当前浏览器URL
        newurl = self.driver2.current_url
        print(newurl)
        self.assertEqual(newurl,"http://byhm.520shq.com/#/login")
        #   对第二个界面进行操作
        loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
        self.m2.is_displayed_ele(loc_user)
        self.l2.loginy("13600008888","a12345")
        self.driver.switch_to.window(window_1)

    def test_invite_05(self):
        '''点击县运营商邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开'''
        self.m.js_scrollTop("2000")
        self.m.click_inviteImg03()
        self.m.click_copyUrl()
        url = self.m.get_url()
        #   获取当前浏览器的句柄
        window_1 = self.driver.current_window_handle
        print(window_1)
        #   用火狐浏览器打开链接
        self.driver2 = webdriver.Firefox()
        self.driver2.get(url)
        self.l2 = LoginFun(self.driver2)
        self.m2 = My(self.driver2)
        #   获取全部浏览器句柄，在进行判断，判断与之前的浏览器句柄是否一致，如果不一致切换到该浏览器窗口
        windows = self.driver2.window_handles
        print(windows)
        for current_window in windows:
            if current_window != window_1:
                self.driver2.switch_to.window(current_window)
        time.sleep(5)
        #   获取当前浏览器URL
        newurl = self.driver2.current_url
        print(newurl)
        self.assertEqual(newurl,"http://byhm.520shq.com/#/login")
        #   对第二个界面进行操作
        loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
        self.m2.is_displayed_ele(loc_user)
        self.l2.loginy("13600008888","a12345")
        self.driver.switch_to.window(window_1)

    def test_invite_06(self):
        '''点击市运营商邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开'''
        self.m.js_scrollTop("2000")
        self.m.click_inviteImg02()
        self.m.click_copyUrl()
        url = self.m.get_url()
        #   获取当前浏览器的句柄
        window_1 = self.driver.current_window_handle
        print(window_1)
        #   用火狐浏览器打开链接
        self.driver2 = webdriver.Firefox()
        self.driver2.get(url)
        self.l2 = LoginFun(self.driver2)
        self.m2 = My(self.driver2)
        #   获取全部浏览器句柄，在进行判断，判断与之前的浏览器句柄是否一致，如果不一致切换到该浏览器窗口
        windows = self.driver2.window_handles
        print(windows)
        for current_window in windows:
            if current_window != window_1:
                self.driver2.switch_to.window(current_window)
        time.sleep(5)
        #   获取当前浏览器URL
        newurl = self.driver2.current_url
        print(newurl)
        self.assertEqual(newurl,"http://byhm.520shq.com/#/login")
        #   对第二个界面进行操作
        loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
        self.m2.is_displayed_ele(loc_user)
        self.l2.loginy("13600008888","a12345")
        self.driver.switch_to.window(window_1)

    def test_invite_07(self):
        '''点击省运营商邀请按钮，进入分享界面，在点击复制链接按钮，在新窗口打开'''
        self.m.js_scrollTop("2000")
        self.m.click_inviteImg01()
        self.m.click_copyUrl()
        url = self.m.get_url()
        #   获取当前浏览器的句柄
        window_1 = self.driver.current_window_handle
        print(window_1)
        #   用火狐浏览器打开链接
        self.driver2 = webdriver.Firefox()
        self.driver2.get(url)
        self.l2 = LoginFun(self.driver2)
        self.m2 = My(self.driver2)
        #   获取全部浏览器句柄，在进行判断，判断与之前的浏览器句柄是否一致，如果不一致切换到该浏览器窗口
        windows = self.driver2.window_handles
        print(windows)
        for current_window in windows:
            if current_window != window_1:
                self.driver2.switch_to.window(current_window)
        time.sleep(5)
        #   获取当前浏览器URL
        newurl = self.driver2.current_url
        print(newurl)
        self.assertEqual(newurl,"http://byhm.520shq.com/#/login")
        #   对第二个界面进行操作
        loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
        self.m2.is_displayed_ele(loc_user)
        self.l2.loginy("13600008888","a12345")
        self.driver.switch_to.window(window_1)