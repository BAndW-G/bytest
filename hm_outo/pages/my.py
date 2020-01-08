from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login import LoginFun
from common.simulation import simu_driver
import time

loc_cut = (By.XPATH,"//div[@class='bottomnav']/div/a[5]")
loc_inviteimg_01 = (By.XPATH,"//div[@class='peopleClass inviteImg']//li[last()-12]")
loc_inviteimg_02 = (By.XPATH,"//div[@class='peopleClass inviteImg']//li[last()-11]")
loc_inviteimg_03 = (By.XPATH,"//div[@class='peopleClass inviteImg']//li[last()-10]")
loc_inviteimg_04 = (By.XPATH,"//div[@class='peopleClass inviteImg']//li[last()-9]")
loc_inviteimg_05 = (By.XPATH,"//div[@class='peopleClass inviteImg']//li[last()-8]")
loc_inviteimg_06 = (By.XPATH,"//div[@class='peopleClass inviteImg']//li[last()-7]")
loc_copy = (By.CSS_SELECTOR,"div.ivtBtn>button:nth-child(1)")
loc_span = (By.CSS_SELECTOR,"span.mint-toast-text")
class My(Base):
    #   我的界面
    def click_cut(self):
        #   切换底部菜单栏  a[1]：首页   a[2]：运营中心  a[3]：用户福利  a[4]：店铺查询  a[5]：我的
        self.clk(loc_cut)

    def click_inviteImg01(self):
        #   点击邀请按钮    -省
        self.clk(loc_inviteimg_01)

    def click_inviteImg02(self):
        #   点击邀请按钮    -市
        self.clk(loc_inviteimg_02)

    def click_inviteImg03(self):
        #   点击邀请按钮    -县
        self.clk(loc_inviteimg_03)

    def click_inviteImg04(self):
        #   点击邀请按钮    -运营商
        self.clk(loc_inviteimg_04)

    def click_inviteImg05(self):
        #   点击邀请按钮    -推广大使
        self.clk(loc_inviteimg_05)

    def click_inviteImg06(self):
        #   点击邀请按钮    -惠盟vip
        self.clk(loc_inviteimg_06)

    def click_copyUrl(self):
        #   点击复制链接
        self.clk(loc_copy)

    def get_copySuccess_text(self):
        #   获取复制成功的文本
        t = self.rtext(loc_span)
        return t

    def get_url(self):
        #   获取复制的URL地址
        t = self.get_att(loc_copy,"data-clipboard-text")
        return t
