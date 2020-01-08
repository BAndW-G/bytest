#   登录函数
from selenium import webdriver
from common.base import Base
from selenium.webdriver.common.by import By
import time

loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
loc_pwd = (By.CSS_SELECTOR,"[placeholder='输入密码']")
loc_click_login =(By.CSS_SELECTOR,".sub")
loc_click_forget = (By.CSS_SELECTOR,".forget")
loc_click_registered = (By.CSS_SELECTOR,".registered")
loc_sucess = (By.CSS_SELECTOR,"[class='mint-toast-text']")
close_home_warm = (By.XPATH,"//div[@class='mint-msgbox-btns']/button[1]")
loc_del_user = (By.TAG_NAME,'i')
class LoginFun(Base):
    #   登录界面元素
    #   def login(self,user="13600002222",pwd="123456"):
    #   #定位输入框
    #   self.sendkeys(loca,user)
    #   self.sendkeys(loca2,pwd)
    #   self.clk(loc3)

    def input_user(self,user="13600002222"):
        #   定位手机号输入框
        # if not isinstance(user,int):
        #     print("----------------")
        # else:
        #     elel = self.sendkeys(loc_user,user)
        #     return elel
        self.sendkeys(loc_user,user)


    def input_pwd(self,pwd="123456"):
        #   定位输入密码输入框
        self.sendkeys(loc_pwd,pwd)

    def click_login_button(self):
        #   点击登录按钮
        self.clk(loc_click_login)

    def click_forget(self):
        #   点击忘记密码按钮
        self.clk(loc_click_forget)

    def click_registered(self):
        #   点击注册按钮
        self.clk(loc_click_registered)

    def get_login_sucess(self):
        #   获取登录返回提示
        #   判断是否有登录成功的提示
        #   unittest自带 assert 断言
        #   self.assertTrue(t == "登录成功")
        #   t = self.driver.find_element_by_css_selector("[class='mint-toast-text']").text
        t = self.rtext(loc_sucess)
        print(t)
        return t

    def click_del_user(self):
        #   点击删除输入框中的值
        self.clk(loc_del_user)

    def get_input_text(self):
        #   获取输入框中输入的值
        t = self.get_att(loc_user,"value")
        print(t)
        return t



    def close_home_warm(self):
        #   关闭首页弹窗
        loc = (By.XPATH,"//div[@class='mint-msgbox-wrapper']/div")
        t = self.get_att(loc,"style")
        time.sleep(3)
        print(t)
        # 判断弹窗是否出现，如果没有出现则不进行关闭弹窗的操作
        if t == "":
            self.clk(close_home_warm)
        else:
            pass

    def login(self,user="13600002222",pwd="123456"):
        self.input_user(user)
        self.input_pwd(pwd)
        self.click_login_button()
        time.sleep(2)
        self.close_home_warm()

    def loginy(self,user="13600002222",pwd="123456"):
        self.input_user(user)
        self.input_pwd(pwd)
        self.click_login_button()


if __name__ == "__main__":
    #   测试
    driver = webdriver.Chrome()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()