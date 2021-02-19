import base
import unittest
from BeautifulReport import BeautifulReport
import CYGL.test_CYGL_Cx
import CYGL.test_CYGL_Add
import CYGL.test_CYGL_Look
import CYGL.test_CYGL_Edit
import CYGL.test_CYGL_Delete


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(CYGL.test_CYGL_Cx.MyTestCase_ZZHL_WHRYGL_Cx('test_ZZHL_WHRYGL_Cx'))
    testunit.addTest(CYGL.test_CYGL_Cx.MyTestCase_ZZHL_WHRYGL_Cx('test_ZZHL_WHRYGL_Fy'))
    testunit.addTest(CYGL.test_CYGL_Add.MyTestCase_ZZHL_WHRYGL_Add('test_ZZHL_WHRYGL_Add1'))
    testunit.addTest(CYGL.test_CYGL_Add.MyTestCase_ZZHL_WHRYGL_Add('test_ZZHL_WHRYGL_Add2'))
    testunit.addTest(CYGL.test_CYGL_Look.MyTestCase_ZZHL_WHRYGL_Look('test_ZZHL_WHRYGL_Look'))
    testunit.addTest(CYGL.test_CYGL_Edit.MyTestCase_ZZHL_WHRYGL_Edit('test_ZZHL_WHRYGL_Edit1'))
    testunit.addTest(CYGL.test_CYGL_Edit.MyTestCase_ZZHL_WHRYGL_Edit('test_ZZHL_WHRYGL_Edit2'))
    testunit.addTest(CYGL.test_CYGL_Delete.MyTestCase_ZZHL_WHRYGL_Logout('test_ZZHL_WHRYGL_Logout1'))
    testunit.addTest(CYGL.test_CYGL_Delete.MyTestCase_ZZHL_WHRYGL_Logout('test_ZZHL_WHRYGL_Logout2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-维护人员管理模块-测试报告',
                  description='智慧护栏平台-维护人员管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../Login/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='盗抢统计分析模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)