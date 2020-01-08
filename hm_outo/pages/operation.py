from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time


loc_cut = (By.XPATH,"//div[@class='bottomnav']/div/a[2]")
loc_task_oper = (By.XPATH,"//div[@class='classify']/a[1]")
loc_seek_oper = (By.XPATH,"//div[@class='classify']/a[2]")
loc_earnings_oper = (By.XPATH,"//div[@class='classify']/a[3]")
loc_contacts_oper = (By.XPATH,"//div[@class='classify']/a[4]")
loc_operation_oper = (By.XPATH,"//div[@class='classify']/a[5]")
loc_audit_oper = (By.XPATH,"//div[@class='classify']/a[6]")
loc_cut_oprator = (By.XPATH,"//div[@class='tabnav']//li[1]/a")
loc_cut_partner = (By.XPATH,"//div[@class='tabnav']//li[2]/a")
loc_task_par = (By.XPATH,"//div[@class='classify']/a[1]")
loc_earnings_par = (By.XPATH,"//div[@class='classify']/a[2]")
loc_operation_par = (By.XPATH,"//div[@class='classify']/a[3]")
loc_oper_earnings = (By.XPATH,"//div[@class='sum']/span")
class Operation(Base):
    #   运营中心
    def click_cut(self):
        #   切换底部菜单栏  a[1]：首页   a[2]：运营中心  a[3]：用户福利  a[4]：店铺查询  a[5]：我的
        self.clk(loc_cut)

    def cut_operator(self):
        #   切换运营商界面
        self.clk(loc_cut_oprator)

    def cut_partner(self):
        #   切换合伙人界面
        self.clk(loc_cut_partner)

    def click_task_oper(self):
        #   点击任务按钮，进入任务界面   -运营商
        self.clk(loc_task_oper)

    def click_seek_oper(self):
        #   点击订单按钮，进入订单界面   -运营商
        self.clk(loc_seek_oper)

    def click_earnings_oper(self):
        #   点击收益明细按钮，进入收益明细界面   -运营商
        self.clk(loc_earnings_oper)

    def click_contacts_oper(self):
        #   点击人脉管理按钮，进入人脉管理界面   -运营商
        self.clk(loc_contacts_oper)

    def click_operation_oper(self):
        #   点击经营信息按钮，进入经营信息界面   -运营商
        self.clk(loc_operation_oper)

    def click_audit_oper(self):
        #   点击升级审核按钮，进入升级审核界面   -运营商
        self.clk(loc_audit_oper)

    def click_task_par(self):
        #   点击任务按钮，进入任务界面   -合伙人
        self.clk(loc_task_par)

    def click_earnings_par(self):
        #   点击收益明细按钮，进入收益明细界面   -合伙人
        self.clk(loc_earnings_par)

    def click_operation_par(self):
        #   点击经营信息按钮，进入经营信息界面   -合伙人
        self.clk(loc_operation_par)

    def get_par_color(self):
        #   获取合伙人字体颜色
        t = self.get_rpg(loc_cut_partner)
        return t

    def get_opr_color(self):
        #   获取运营商字体颜色
        t = self.get_rpg(loc_cut_oprator)
        return t

    def get_oper_earning(self):
        #   获取运营商的发展总收益数值
        t = self.rtext(loc_oper_earnings)
        t = int(t[1:])
        return t

    def get_gains_oper(self,n=0):
        #   获取运营商的收益明细页面的数值
        n =+ 1
        ele = ("//li[%s]//span[@class='price']" %n)
        t = driver.find_element_by_xpath(ele)
        t = int(t[2:])










if __name__ == "__main__":
    #   测试
    driver = simu_driver()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()
    cs = Operation(driver)
    cs.click_cut()
    time.sleep(5)
    cs.get_oper_earning()
