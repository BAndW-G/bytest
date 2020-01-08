from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time

loc_download =(By.XPATH,"//div[@class='down-load']")
loc_x =(By.XPATH,"//div[@class='guide']/div/i")
loc_banner =(By.XPATH,"//div[@class='column-img']/div/div/div/a/img")
loc_voucher = (By.XPATH,"//h1")
loc_orientation = (By.XPATH,"//header[@class='mint-header']/a")
loc_merchant = (By.CSS_SELECTOR,"div.cpbox")
loc_orien_text = (By.XPATH,"//header/h1[1]")
loc_home_input = (By.XPATH,"//a/input")
loc_input_text = (By.XPATH,"//header/div[2]")
loc_private_letter = (By.XPATH,"//div[@slot]")
loc_letter_text = (By.XPATH,"//h1")
loc_ad_img = (By.XPATH,"//div[@class='indexFl']/img")
loc_cut = (By.XPATH,"//div[@class='bottomnav']/div/a[2]")
loc_prompt_order = (By.XPATH,"//img[@class='go-pay']")
loc_order_text = (By.XPATH,"//div[@class='top_nav']/span")
loc_active_color = (By.XPATH,"//div[@class='nav-list']//div[@class='mint-swipe-indicator is-active']")
class Home(Base):
    #   首页元素    //*[@id="app"]/div[1]/div[7]/div/div/img
    def tap_download(self):
        #   点击下载按钮  无法生效
        self.tap_element(loc_download)

    def click_x(self):
        #   点击下载按钮旁边的x按钮
        self.clk(loc_x)

    def click_banner(self):
        #   点击首页banner图
        self.clk(loc_banner)

    def get_voucher(self):
        #   获取百业专区导航栏文本
        t = self.rtext(loc_voucher)
        print(t)
        return t

    def click_orientation(self,):
        #   点击当前位置图标
        self.clk(loc_orientation)

    def get_orie_home_text(self):
        #   获取当前位置
        t = self.rtext(loc_orientation)
        return t

    def get_orien_text(self):
        #   获取选择位置界面导航栏文本
        t = self.rtext(loc_orien_text)
        print(t)
        return t

    def click_home_input(self):
        #   跳转到搜索界面
        self.clk(loc_home_input)

    def get_input_text(self):
        #   获取搜索按钮文本
        t = self.rtext(loc_input_text)
        return t

    def click_private_letter(self):
        #   跳转到私信界面
        self.clk(loc_private_letter)

    def get_letter_text(self):
        #   获取搜索按钮文本
        t = self.rtext(loc_letter_text)
        return t

    def is_displayed_ad(self):
        #   当当前地区无商家时，首页展示加盟图片
        d = self.is_displayed_ele(loc_ad_img)
        return d

    def is_displayed_cp(self):
        #   当当前地区有商家时,页面是否存在
        d = self.is_displayed_ele(loc_merchant)
        return d

    def click_cut(self):
        #   切换底部菜单栏  a[1]：首页   a[2]：运营中心  a[3]：用户福利  a[4]：店铺查询  a[5]：我的
        self.clk(loc_cut)

    def click_prompt_order(self):
        #   未支付订单提示
        self.clk(loc_prompt_order)

    def get_order_text(self):
        #   获取订单界面文本
        t = self.rtext(loc_order_text)
        return t

    def get_color_value(self):
        #   获取界面元素的color值
        t = self.get_back_color(loc_active_color)
        return t



if __name__ == "__main__":
    #   测试
    driver = simu_driver()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()
    cs = Home(driver)
    cs.get_color_value()
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)