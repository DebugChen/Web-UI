import base
import unittest
from BeautifulReport import BeautifulReport
import ZHGL.test_ZHGL_Cx
import ZHGL.test_ZHGL_Add
import ZHGL.test_ZHGL_Edit
import ZHGL.test_ZHGL_Look
import ZHGL.test_ZHGL_Logout
import ZHGL.test_ZHGL_Initialize


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(ZHGL.test_ZHGL_Cx.MyTestCase_ZHHL_ZHGL_Cx('test_ZHHL_ZHGL_Cx'))
    testunit.addTest(ZHGL.test_ZHGL_Cx.MyTestCase_ZHHL_ZHGL_Cx('test_ZHHL_ZHGL_Fy'))
    testunit.addTest(ZHGL.test_ZHGL_Add.MyTestCase_ZHHL_ZHGL_Add('test_ZHHL_ZHGL_Add1'))
    testunit.addTest(ZHGL.test_ZHGL_Add.MyTestCase_ZHHL_ZHGL_Add('test_ZHHL_ZHGL_Add2'))
    testunit.addTest(ZHGL.test_ZHGL_Initialize.MyTestCase_ZHHL_ZHGL_Initialize('test_ZHHL_ZHGL_Initialize'))
    testunit.addTest(ZHGL.test_ZHGL_Look.MyTestCase_ZHHL_ZHGL_Look('test_ZHHL_ZHGL_Look'))
    testunit.addTest(ZHGL.test_ZHGL_Edit.MyTestCase_ZHHL_ZHGL_Edit('test_ZHHL_ZHGL_Edit1'))
    testunit.addTest(ZHGL.test_ZHGL_Edit.MyTestCase_ZHHL_ZHGL_Edit('test_ZHHL_ZHGL_Edit2'))
    testunit.addTest(ZHGL.test_ZHGL_Logout.MyTestCase_ZHHL_ZHGL_Logout('test_ZHHL_ZHGL_Logout1'))
    testunit.addTest(ZHGL.test_ZHGL_Logout.MyTestCase_ZHHL_ZHGL_Logout('test_ZHHL_ZHGL_Logout2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-账户管理模块-测试报告',
                  description='智慧护栏平台-账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../ZHGL/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='APP账户管理模块-测试用例执行情况')
    # #执行测试用例
    # #执行测试用例
    # runner.run(testunit)