from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time

loc_cut = (By.XPATH,"//div[@class='bottomnav']/div/a[3]")
loc_order = (By.XPATH,"//header/div[2]/button[2]")
loc_return = (By.XPATH,"//button//i")
loc_renew = (By.XPATH,"//header/div[2]/button[1]")
loc_renew_return = (By.XPATH,"//header//button")
loc_renew_buy = (By.CSS_SELECTOR,"div.pay-btn")
loc_cards = (By.CSS_SELECTOR,"button.search-btn")
loc_cards_use = (By.XPATH,"//div[@class='xf']/../button[1]")
loc_cards_donation = (By.XPATH,"//div[@class='xf']/../button[2]")
loc_balance = (By.CSS_SELECTOR,"div.xf>i")
loc_addUp = (By.XPATH,"//li[1]//p[@class='count']")
loc_use = (By.XPATH,"//li[3]//p[@class='count']")
loc_gain_cards = (By.XPATH,"//ul[@class='managebtn']/li[1]")
loc_senk_cards = (By.XPATH,"//ul[@class='managebtn']/li[2]")
loc_ul = (By.XPATH,"//ul[@class='list']")
loc_num = (By.CSS_SELECTOR,"ul.manage>li:nth-child(2)>p.count")
class Benefits(Base):
    #   用户福利
    def click_cut(self):
        #   切换底部菜单栏  a[1]：首页   a[2]：运营中心  a[3]：用户福利  a[4]：店铺查询  a[5]：我的
        self.clk(loc_cut)

    def click_order(self):
        #   点击订单按钮进入订单界面
        self.clk(loc_order)

    def click_return(self):
        #   点击界面左上角返回按钮
        self.clk(loc_return)

    def click_renew(self):
        #   点击进入续费界面
        self.clk(loc_renew)

    def click_renew_return(self):
        #   点击续费界面返回按钮
        self.clk(loc_renew_return)

    def click_renew_buy(self):
        #   点击立即购买
        self.clk(loc_renew_buy)

    def enabled_renew_buy(self):
        #   判断立即购买按钮是否可用
        t = self.is_enabled_ele(loc_renew_buy)
        return t

    def click_cards_particulars(self):
        #   点击进入消费券详情界面
        t = self.is_displayed_ele(loc_cards)
        self.clk(loc_cards)
        print(t)

    def click_cards_use(self):
        #   跳转到消费券使用界面
        self.clk(loc_cards_use)

    def click_cards_donation(self):
        #   跳转到消费券转赠界面
        self.clk(loc_cards_donation)

    def get_balance_text(self):
        #   获取消费券余额
        t = self.rtext(loc_balance)
        return float(t)

    def get_addUp_text(self):
        #   获取累计消费券额度
        t = self.rtext(loc_addUp)
        return float(t)

    def get_use_text(self):
        #   获取已使用消费券额度
        t = self.rtext(loc_use)
        return float(t)

    def click_gain_cards(self):
        #   显示消费券的获赠记录
        self.clk(loc_gain_cards)

    def click_senk_cards(self):
        #   显示消费券的送出记录
        self.clk(loc_senk_cards)

    def get_list_total(self):
        #   获取次数数量
        t = self.get_list_number(loc_ul)
        print(t)
        return t

    def get_num(self):
        #   获取界面显示的次数
        t = self.rtext(loc_num)
        return t

if __name__ == "__main__":
    #   测试
    driver = simu_driver()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()
    cs = Benefits(driver)
    cs.click_cut()
    time.sleep(5)
    cs.click_cards_particulars()
    cs.get_list_num()