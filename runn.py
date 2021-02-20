# 导包
import time
import unittest

# 生成测试套件(组装用例)

from htmlfile.HTMLTestReportCN import HTMLTestRunner
from tpshop_login3 import TestAdd2

suite = unittest.TestSuite()

#方法1
# suite.addTest(unittest.makeSuite(TestAdd2))

#方法2
suite.addTest(TestAdd2("test_add_011"))
suite.addTest(TestAdd2("test_add_022"))
suite.addTest(TestAdd2("test_add_033"))

# 注意1:用例的组装方法可以根据需求灵活选择
# suite = unittest.TestLoader().discover("./cases/", pattern="soft*.py")
# suite = unittest.defaultTestLoader.discover("./cases/", pattern="soft*.py")

# 报告存放路径及报告名称
# 注意:报告存放路径必须要先手动创建,否则报错信息 No such file or directory
# report_path = "./report/WebAutoTestReport.html"

# 注意2:可以通过 time.strftime() 方法获取时间戳防止报告重名
report_path = "./report/WebAutoTestReport_{}.html".format(time.strftime("%Y%m%d_%H%M%S"))

# 写入报告
# 打开文件写入流
with open(report_path, "wb") as f:
    # 初始化执行对象
    # 注意3:
    # 1.verbosity=2(表示执行日志的输出格式,默认 1(简要模式),可选 2(详细模式))
    # 2.title= (生成的报告内容的标题设置)
    # 3.description= (测试环境的相关描述信息)
    runner = HTMLTestRunner(stream=f, verbosity=2, title="Web自动化测试报告", description="macOS, Firefox, Python")
    # 调用执行方法
    runner.run(suite)