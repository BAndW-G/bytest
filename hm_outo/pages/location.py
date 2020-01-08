from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
from selenium.webdriver.common.action_chains import ActionChains
import time

loc_orientation = (By.XPATH,"//header[@class='mint-header']/a")
loc_current_location = (By.XPATH,"//div[@class='lp']")
loc_back_home = ("xpath","//button/span")
class Location(Base):
    #   地区定位页面
    def click_orientation(self):
        #   点击当前位置图标
        self.clk(loc_orientation)

    def click_current_location(self):
        #   当前定位
        self.clk(loc_current_location)

    def get_loca_text(self):
        #   地址信息
        t = self.rtext(loc_current_location)
        return t[5:]

    def click_switch_area(self,p="广东",city="广州",county="天河"):
        #   切换地区
        loc_area_p = (By.XPATH,"//span[contains(text(),'%s')]"%p)
        loc_area_city = ("xpath","//span[contains(text(),'%s')]"%city)
        loc_area_county = ("xpath","//span[contains(text(),'%s')]"%county)
        self.clk(loc_area_p)
        self.clk(loc_area_city)
        self.clk(loc_area_county)

    def click_back_home(self):
        #   返回首页
        self.clk(loc_back_home)


if __name__ == "__main__":
    #   测试
    driver = simu_driver()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()
    loc_orientation = (By.XPATH,"//header[@class='mint-header']/a")
    cs.clk(loc_orientation)
    cs = Location(driver)
    cs.click_switch_area()