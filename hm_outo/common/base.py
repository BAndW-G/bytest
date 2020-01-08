from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Base():
    '''基于原生selenium的二次封装'''
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 15
        self.poll_frequency=0.5

    def findElement(self,loctor):
        #   定位单个元素
        #   loctor=("by,value")
        #   WebDriverWait(driver,timeout,poll_frequency).until(lambda x: x.find_element_by_id("someId"))
        #   *的作用就是把list或者元祖分开传入
        if not isinstance(loctor,tuple):
            print('loctor参数类型输入错误，必须传元祖类型：loctor=("by,value")')
        else:
            print('定位方式-》%s,value值-》%s'%(loctor[0],loctor[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(EC.presence_of_element_located(loctor))
            return ele

    def findElements(self,loctor):
        #   定位组一组元素
        ele = WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(lambda x: x.find_elements(*loctor))
        return ele

    def findElementEC(self,loctor):
        #   用EC里的方法定位元素
        ele = WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(EC.presence_of_element_located(loctor))
        return ele

    def sendkeys(self,loctor,text):
        #   定义send_keys方法，text是传入的内容
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def clk(self,loctor):
        #   定义click方法
        ele = self.findElement(loctor)
        ele.click()

    def rtext(self,loctor):
        #   获取元素文本值
        text = self.findElement(loctor).text
        return text

    def get_att(self,loctor,element):
        #   获取元素属性值     填写value可以获取到input输入框的内容
        ele = self.findElement(loctor).get_attribute(element)
        return ele

    def locxy_click(self,dr,x,y,left_click=True):
        #   dr:浏览器
        #   x:页面x坐标
        #   y:页面y坐标
        #   left_click:True为鼠标左键点击，否则为右键
        if left_click:
            ActionChains(dr).move_by_offset(x,y).click().perform()
        else:
            ActionChains(dr).move_by_offset(x,y).context_click().perform()
        #   将鼠标恢复到移动前的位置
        ActionChains(dr).move_by_offset(-x,-y).perform()

    def move_to_element(self,loctor):
        #   鼠标悬停    无法调用
        ele = self.findElement(loctor)
        ActionChains(driver).move_to_element(ele).perform()

    def tap_element(self,loctor):
        #   模拟手指触摸屏幕元素  无法调用
        ele = self.findElement(loctor)
        tas = TouchActions(driver)
        tas.tap(ele).perform()

    def is_displayed_ele(self,loctor):
        #   判断元素是否隐藏
        ele = self.findElement(loctor).is_displayed()
        print(ele)
        return ele

    def is_enabled_ele(self,loctor):
        #   判断元素是否可用
        ele = self.findElement(loctor).is_enabled()
        return ele

    def is_staleness_of(self,loctor):
        #   不会用
        ele = WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(EC.staleness_of(loctor))
        return ele

    def is_text_in_element(self,loctor,_text):
        #   对元素的text文本进行判断，返回bool值
        ele = WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(EC.text_to_be_present_in_element(loctor,_text))
        return ele

    def isElementPresent(self,locta):
        #   查询界面上是否有ele元素存在     不可用
        try:
            ele = self.findElement(locta)

        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True

    def get_back_color(self,loctor):
        #   获取元素的color属性，已元组（tuple）的方式输出
        ele = self.findElement(loctor)
        t= ele.value_of_css_property("background-color")
        #   从第5位开始取值
        rpga = t[4:]
        #   将字符串转换成列表
        r = list(eval(rpga))
        #   去除最后一位
        rpg = r[:-1]
        print(rpg)
        #   返回元祖类型
        return tuple(rpg)

    def get_color(self,loctor):
        #   获取元素的color属性，已元组（tuple）的方式输出
        ele = self.findElement(loctor)
        t= ele.value_of_css_property("color")
        #   从第5位开始取值
        rpga = t[4:]
        #   将字符串转换成列表
        r = list(eval(rpga))
        #   去除最后一位
        rpg = r[:-1]
        print(rpg)
        #   返回元祖类型
        return tuple(rpg)

    def RGB_to_Hex(self,RGB):
        #   :param RGBA: a tuple, exp: (59, 201, 255, 255)
        #   :return hex_str: a str, exp: #3BC9FFFF
        hex_str = '#'
        for i in RGB:
            num = int(i) # 将RGBA的数值转换成数字类型
            hex_str = hex_str + str(hex(num))[2:].replace('x', '0').upper()
        # print(hex_str)
        return hex_str.lower()

    def get_back_rpg(self,loctor):
        #   获取界面上元素的颜色
        rpg = self.get_back_color(loctor)
        h = self.RGB_to_Hex(rpg)
        print(h)
        return h

    def get_rpg(self,loctor):
        #   获取界面上元素的颜色
        rpg = self.get_color(loctor)
        h = self.RGB_to_Hex(rpg)
        print(h)
        return h

    def get_list_number(self,loctor):
        #   获取ul中li的总数，并返回
        ul = self.findElement(loctor)
        lis = ul.find_elements_by_xpath("li")
        return len(lis)

    def new_win(self,url="http://www.baidu.com"):
        # 打开新窗口
        js = "window.open('%s');" %url
        self.driver.execute_script(js)

    def cut_win(self):
        # 切换到新打开的窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    def cutBack_win(self):
        # 切回到最初打开的窗口
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def js_scrollTop(self,t):
        #  js模拟鼠标滑轮下滑
        js="var q=document.documentElement.scrollTop=%s"%t
        self.driver.execute_script(js)

    def js_scrollLeft(self,t):
        #  js模拟鼠标滑轮下滑
        js="var q=document.documentElement.scrollLeft=%s"%t
        self.driver.execute_script(js)
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://byhm.520shq.com/#/login")
    cs = Base(driver)
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)