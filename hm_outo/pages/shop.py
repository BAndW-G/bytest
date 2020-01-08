from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time


loc_click_shop = (By.CSS_SELECTOR,"div.cplist>div>img")
loc_click_ele = (By.CSS_SELECTOR,"div.cplist>div:nth-child(2)")
loc_shop_text = (By.CSS_SELECTOR,"header>h1.mint-header-title")
loc_click_more = (By.XPATH,"//header/div[2]//span")
loc_top = (By.CSS_SELECTOR,"div.topTab")
loc_click_benefits = (By.CSS_SELECTOR,"div.topTab>p")
loc_click_share = (By.CSS_SELECTOR,"div.topTab>p:nth-child(2)")
loc_get_share = (By.CSS_SELECTOR,"span.mint-toast-text")
loc_look_img = (By.CSS_SELECTOR,"a.col")
loc_shop_name = (By.CSS_SELECTOR,"div.topname>span")
loc_navigation = (By.CSS_SELECTOR,"div.address")
loc_navigation_text = (By.XPATH,"//header[@class='mint-header is-fixed']//h1")
loc_navigation_back = (By.XPATH,"//header[@class='mint-header is-fixed']/div[1]")
loc_discount_stores = (By.CSS_SELECTOR,"div.detailed>*>ul>li:nth-child(1)")
loc_surroundings = (By.CSS_SELECTOR,"div.detailed>*>ul>li:nth-child(2)")
loc_information = (By.CSS_SELECTOR,"div.detailed>*>ul>li:nth-child(3)")

class Homeshop(Base):
    #   首页商家
    def click_img_shop(self):
        #   点击首页商家图片
        self.clk(loc_click_shop)

    def click_ele_shop(self):
        #   点击首页的商家信息其他元素
        self.clk(loc_click_ele)

    def get_shop_text(self):
        #   获取导航栏文本
        self.rtext(loc_shop_text)

    def click_more(self):
        #   点击右上角的更多按钮
        self.clk(loc_click_more)

    def display(self):
        #   判断弹窗是否展开
        t = self.is_displayed_ele(loc_top)
        return t

    def click_benefits(self):
        #   点击跳转用户福利
        self.click_more()
        self.clk(loc_click_benefits)

    def click_share(self):
        #   点击店铺分享
        self.click_more()
        self.clk(loc_click_share)

    def get_share_text(self):
        #   获取分享提示语
        t = self.rtext(loc_get_share)
        print(t)
        return t

    def click_look_img(self):
        #   点击查看全部图片
        self.clk(loc_look_img)

    def get_shop_name(self):
        #   获取商家名称
        self.rtext(loc_shop_name)

    def click_navigation(self):
        #   点击导航按钮
        self.clk(loc_navigation)

    def get_navigation_text(self):
        #   获取导航界面文本   地图显示
        t = self.rtext(loc_navigation_text)
        return t

    def click_navigation_back(self):
        #   返回
        self.clk(loc_navigation_back)

    def cilck_discount_stores(self):
        #   点击店铺优惠
        self.clk(loc_discount_stores)

    def click_surroundings(self):
        #   点击环境按钮
        self.clk(loc_surroundings)

    def click_information(self):
        #   点击商家信息按钮
        self.clk(loc_information)

    def get_discount_class(self):
        #   获取店铺优惠的class属性
        t = self.get_att(loc_discount_stores,"class")
        return t

    def get_surroundings_class(self):
        #   获取环境的class属性
        t = self.get_att(loc_surroundings,"class")
        return t

    def get_information_class(self):
        #   获取商家信息的class属性
        t = self.get_att(loc_information,"class")
        return t

loc_cut = (By.XPATH,"//div[@class='bottomnav']/div/a[4]")
loc_area = (By.CSS_SELECTOR,"div.nav>button")
loc_progress  = (By.CSS_SELECTOR,"div.nav>button:nth-child(2)")
loc_first_shop = (By.CSS_SELECTOR,"div.list>div")
loc_upload_img = (By.CSS_SELECTOR,"div.upload-icon")
loc_upload_img_input = (By.XPATH,"//div[@class='shop']/div[last()]//input")
loc_click_alter = (By.CSS_SELECTOR,"div.sub>button")
loc_X = (By.XPATH,"//div[@class='shop']/div[last()-1]/i")
class Shop(Base):
    #   店铺查询
    def click_cut(self):
        #   切换底部菜单栏  a[1]：首页   a[2]：运营中心  a[3]：用户福利  a[4]：店铺查询  a[5]：我的
        self.clk(loc_cut)

    def click_area_shop(self):
        #   点击区域内商家
        self.clk(loc_area)

    def click_progress_shop(self):
        #   点击发展商家
        self.clk(loc_progress)

    def get_pro_color(self):
        #   获取发展商家按钮的颜色
        c = self.get_rpg(loc_progress)
        return c

    def click_first_shop(self):
        #   点击发展商家的第一个商家
        self.clk(loc_first_shop)

    def sendkey_img(self):
        #   上传图片
        self.sendkeys(loc_upload_img_input,r"d:\733373.jpg")

    def click_X(self):
        #   定位倒数第一张图片的删除按钮
        self.clk(loc_X)

    def click_alter(self):
        #   点击提交更改
        self.clk(loc_click_alter)

if __name__ == "__main__":
    driver = simu_driver()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()
    cs = Shop(driver)
    cs.click_cut()
    cs.click_progress_shop()
    cs.click_first_shop()
    time.sleep(2)
    cs.sendkey_img()