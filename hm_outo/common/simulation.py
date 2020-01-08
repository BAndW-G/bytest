from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def simu_driver():
    mobile_emulation = {"deviceName":"Galaxy S5"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
    return driver

