from common.base import Base
from selenium.webdriver.common.by import By
from pages.home import Home
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time

loc_seek = (By.XPATH,"//div[@class='searhed']/input")
loc_seek_input = (By.XPATH,"//header[@class='mint-header']/div[2]")
loc_seek_x= (By.XPATH,"//div[@class='searhed']/i[2]")
loc_clear_history = (By.XPATH,"//span[@class='clear']")
loc_click_history = (By.XPATH,"//span[@class='search-list']")
loc_back_home = (By.XPATH,"//button/span")
loc_seek_text = (By.XPATH,"//div[@class='mint-toast is-placemiddle'][2]/span")
class Seek(Base):
    #   搜索界面元素
    def click_seek(self):
        #   选中搜索栏
        self.clk(loc_seek)

    def send_seek(self,text):
        #   向搜索栏中输入text
        self.sendkeys(loc_seek,text)

    def click_seek_input(self):
        #   点击搜索按钮 （进入搜索界面）
        self.clk(loc_seek_input)

    def click_del_input(self):
        #   点击删除按钮。删除搜索框内容
        self.clk(loc_seek_x)

    def click_clear_history(self):
        #   点击清除按钮，清除历史记录。（只有在进行过搜索后才会有历史记录）
        self.clk(loc_clear_history)

    def click_history(self):
        #   点击历史记录，搜索商家。（进入搜索界面）（只有在进行过搜索后才会有历史记录）
        self.clk(loc_click_history)

    def click_back(self):
        #   返回上一页
        self.clk(loc_back_home)

    def get_seek_text(self):
        #   获取搜索提示文本    请输入搜索关键词。
        t = self.rtext(loc_seek_text)
        return t







if __name__ == "__main__":
    #   测试
    driver = simu_driver()
    driver.get('http://byhm.520shq.com/#/login')
    driver.maximize_window()
    cs = LoginFun(driver)
    cs.login()
    cs = Home(driver)
    cs.click_home_input()
    cs = Seek(driver)
    cs.click_seek()