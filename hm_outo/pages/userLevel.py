from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time
loc = (By.CSS_SELECTOR,"p.level>*")
loc2 = (By.XPATH,"//p[@class='level']/span[2]")
loc3 = (By.XPATH,"//p[@class='level']/span")
class Userlevel(Base):
    #   获取当前用户等级
    def ulevel(self):
        lis = self.findElements(loc)
        if len(lis) == 2:
            t = self.rtext(loc2)
            print("合伙人用户")
        else:
            t = self.rtext(loc3)
            print("非合伙人用户")
        return t