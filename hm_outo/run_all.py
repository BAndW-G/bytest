import unittest
import threading
from common import HTMLTestRunner
#用例存放的路径
casePath = "D:\py\hm_outo\case"
#匹配规则(test开头，.py的文件)
rule = "test*.py"
#报告路径
report = "D:\py\hm_outo\\report\\"+"report.html"
#读取路径,以二进制去写入
fp = open(report,"wb")
#通过unittest下的discover方法同时运行多个测试用例脚本
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title="报告的名称",
                                       description="描述你的用例")
runner.run(discover)
#关闭
fp.close()