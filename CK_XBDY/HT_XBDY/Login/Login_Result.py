import base
import unittest
from BeautifulReport import BeautifulReport
import Login.test_LoginExit
import Login.test_Xgmm


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(Login.test_LoginExit.MyTestCase_XBDY_LoginExit('test_XBDY_Login'))
    testunit.addTest(Login.test_LoginExit.MyTestCase_XBDY_LoginExit('test_XBDY_Exit'))
    testunit.addTest(Login.test_Xgmm.MyTestCase_XBDY_Xgmm('test_XBDY_Xgmm1'))
    testunit.addTest(Login.test_Xgmm.MyTestCase_XBDY_Xgmm('test_XBDY_Xgmm2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-登录模块-测试报告',
                  description='新北斗云平台-供应商列表模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 运行用例filename=报告名称，
    # description=所有用例总的名称，
    # report_path=报告路径,如果不填写默认当前执行文件目录，
    # theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种

    # # 定义测试报告存放路径
    # fp=open('../LSTZ/image1/result2.html','wb')
    # # 定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='客户信息管理模块-测试用例执行情况')
    # # 执行测试用例
    # runner.run(testunit)