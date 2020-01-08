from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login import LoginFun


loc_user = (By.CSS_SELECTOR,"[placeholder='输入手机号码']")
loc_clk_vc = (By.XPATH,"//i[@class='code01']")
loc_vc = (By.CSS_SELECTOR,"[placeholder='输入验证码']")
loc_pwd = (By.CSS_SELECTOR,"[placeholder='输入密码']")
loc_icon_eye = (By.XPATH,"html/body/div/div/div/div/div/div/i")
loc_button = (By.CSS_SELECTOR,".sub.subhse")
loc_back_login = (By.XPATH,"//div[@class='thr-center']/span")
loc_sucessx = (By.XPATH,"/html/body/div[3]/span")


class Register(Base):
    '''注册方法'''
    def input_user(self,user):
        #   定位手机号输入框
        self.sendkeys(loc_user,user)

    def click_vc(self):
        #   定位获取验证码按钮
        self.clk(loc_clk_vc)

    def input_vc(self,vc):
        #   定位验证码输入框
        self.sendkeys(loc_vc,vc)

    def input_pwd(self,pwd):
        #   定位密码输入框
        self.sendkeys(loc_pwd,pwd)

    def click_icon_eye(self):
        #   定位掩码显示图标
        self.clk(loc_icon_eye)

    def click_button(self):
        #   定位注册按钮
        self.clk(loc_button)

    def click_back_login(self):
        #   返回登录界面
        self.clk(loc_back_login)

    def get_sucess(self):
        #   获取注册返回提示
        t = self.rtext(loc_sucessx)
        print(t)
        return t




if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://byhm.520shq.com/#/login")
    cs = LoginFun(driver)
    cs1 = Register(driver)
    cs.click_registered()
    # cs1.input_user(user = "13608005555")
    cs1.click_vc()
    # cs1.input_vc(vc="1234")
    # cs1.input_pwd("asdadasd")
    # cs1.click_icon_eye()
    # cs1.click_button()
    # cs1.click_back_login()
    # cs1.get_sucess()
