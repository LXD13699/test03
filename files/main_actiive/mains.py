import  unittest
#添加测试套件
from files.case.add_case import AddCase
from files.case.del_case import delCase
from files.case.login_case import LoginCase
from files.lib.HTMLTestRunner_CN import HTMLTestRunner
from files.tool.email_tool import SendEmail

suit = unittest.TestSuite()
#创建加载类
testloader =unittest.TestLoader()
#返回加载类
login = testloader.loadTestsFromTestCase(LoginCase)
adds = testloader.loadTestsFromTestCase(AddCase)
#添加
suit.addTest(login)
suit.addTest(adds)
# unittest.TextTestRunner().run(suit)

report_path = "D:\\software\\pycharmTest\\test03\\files\\report\\report.html"
with open(report_path,mode="wb") as f:
    HTMLTestRunner(f).run(suit)

SendEmail().send_email(report_path,"自动化")
