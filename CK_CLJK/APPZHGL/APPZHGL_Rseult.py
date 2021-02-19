import base
import unittest
from BeautifulReport import BeautifulReport
import APPZHGL.test_APPZHGL_Cx
import APPZHGL.test_APPZHGL_Edit


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(APPZHGL.test_APPZHGL_Cx.MyTestCase_CLJK_APPZHGL_Cx('test_CLJK_APPZHGL_Cx'))
    testunit.addTest(APPZHGL.test_APPZHGL_Cx.MyTestCase_CLJK_APPZHGL_Cx('test_CLJK_APPZHGL_Fy'))
    testunit.addTest(APPZHGL.test_APPZHGL_Edit.MyTestCase_CLJK_APPZHGL_Edit('test_CLJK_APPZHGL_Edit1'))
    testunit.addTest(APPZHGL.test_APPZHGL_Edit.MyTestCase_CLJK_APPZHGL_Edit('test_CLJK_APPZHGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-APP账户管理模块-测试报告',
                  description='车辆监控平台-APP账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../APPZHGL/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='APP账户管理模块-测试用例执行情况')
    # #执行测试用例
    # #执行测试用例
    # runner.run(testunit)