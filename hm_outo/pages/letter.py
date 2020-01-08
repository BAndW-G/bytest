from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time



loc_all_letter = (By.XPATH,"//ul[@class='managebtn']/li[1]")
loc_earnings_letter = (By.XPATH,"//ul[@class='managebtn']/li[2]")
loc_del_letter = (By.XPATH,"//div[@class='itembox']//li[1]//span[2]")
loc_click_back = (By.XPATH,"//div[1]/button")
class Letter(Base):
    #   私信界面
    def click_all_letter(self):
        #   点击切换至全部私信
        self.clk(loc_all_letter)

    def click_earnings_letter(self):
        #   点击切换至收益私信
        self.clk(loc_earnings_letter)

    def click_del_letter(self):
        #   点击删除私信      li[1]是第一条，li[2]是第二条，以此类推。。。
        self.clk(loc_del_letter)

    def click_back(self):
        #   点击返回按钮
        self.clk(loc_click_back)