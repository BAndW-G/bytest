from selenium import webdriver
from pages.login import LoginFun
import unittest
from common.simulation import simu_driver
from common.read_xlsx import ExcelUtil
import ddt
import os

'''
    1   输入正确账号，正确密码，点击登录，提示登录成功
    2   输入正确账号，不输入密码，点击登录，提示输入登录密码！
    3   输入正确账号，输入错误密码，点击登录，提示用户不存在或密码错误
    4   不输入账号，输入密码，点击登录，提示请输入登录手机号码！
    5   输入错误账号，输入密码，点击登录，提示用户不存在或密码错误
    6   点击删除已输入账号按钮，输入账号被删除
'''

testdatas=[
    {"user":"13600002222","pwd":"123456","sucess":"登录成功"},
    {"user":"13600002222","pwd":"","sucess":"请输入登录密码！"},
    {"user":"13600002222","pwd":"111111","sucess":"用户不存在或密码错误"},
    {"user":"","pwd":"123456","sucess":"请输入登录手机号码！"},
    {"user":"13601111112","pwd":"123456","sucess":"用户不存在或密码错误"},
]

# propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# filepath =os.path.join(propath,"common","login.xlsx")
# print(filepath)
# data = ExcelUtil(filepath)
# testdatas = data.dict_data()
# print(testdatas)

@ddt.ddt
class Login_Test(unittest.TestCase):
    '''登录页面测试'''

    @classmethod
    def setUpClass(cls):
        #打开浏览器
        cls.driver = webdriver.Chrome()
        #实例化 LoginFun
        cls.loginx = LoginFun(cls.driver)

    def setUp(self):
        self.driver.get("http://byhm.520shq.com/#/login")
        self.driver.maximize_window()

    def login_case(self,user,pwd,sucess):
        '''    登录步骤    '''
        self.loginx.loginy(user,pwd)
        t = self.loginx.get_login_sucess()
        print("获取结果:%s"%t)
        # 判断是否有登录成功的提示
        # unittest自带 assert 断言
        self.assertTrue(t == sucess)

    @ddt.data(*testdatas)
    def test_login_0105(self,data):
        '''     输入账号，密码，点击登录    '''
        print("--------开始测试-------")
        print("测试数据 %s"%data)
        self.login_case(data["user"],data["pwd"],data["sucess"])
        print("---------结束测试-------")

    #     def test_login_2(self,data):
    #     '''     输入正确账号，不输入密码，点击登录    '''
    #     data2 = testdatas[1]
    #     print("测试数据: %s"%data2)
    #     self.login_case(data["user"],data["pwd"],data["sucess"])
    #
    # def test_login_3(self,data):
    #     '''     不输入账号，输入密码，点击登录    '''
    #     data3 = testdatas[2]
    #     print("测试数据 %s"%data3)
    #     self.login_case(data["user"],data["pwd"],data["sucess"])

    def test_login_6(self):
        '''点击删除已输入账号按钮，输入账号被删除 '''

        print("--------开始测试-------")

        self.loginx.input_user()
        t = self.loginx.get_input_text()
        print("测试数据 %s "%t)
        self.assertTrue(t,"13600002222")
        self.loginx.click_del_user()
        s = self.loginx.get_input_text()
        print("测试数据 %s"%s)
        self.assertTrue(t,None)
        print("---------结束测试-------")


    def tearDown(self):
        #清空cookies，退出登录
        self.driver.delete_all_cookies()
        #刷新界面
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()