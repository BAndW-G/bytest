# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")

time.sleep(3)
# 默认在取消按钮上，先切换到保存文件上
k = PyKeyboard()

# 发送tab
k.press_key(k.tab_key)
k.release_key(k.tab_key)

time.sleep(3)
# 发送回车
k.press_key(k.enter_key)
k.release_key(k.enter_key)