import base
import unittest
from BeautifulReport import BeautifulReport
import WHDW.test_WHDW_Cx
import WHDW.test_WHDW_Add
import WHDW.test_WHDW_Look
import WHDW.test_WHDW_Fwzz
import WHDW.test_WHDW_Logout


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(WHDW.test_WHDW_Cx.MyTestCase_ZZHL_WHDWGL_Cx('test_ZZHL_WHDWGL_Cx'))
    testunit.addTest(WHDW.test_WHDW_Cx.MyTestCase_ZZHL_WHDWGL_Cx('test_ZZHL_WHDWGL_Fy'))
    testunit.addTest(WHDW.test_WHDW_Add.MyTestCase_ZZHL_WHDWGL_Add('test_ZZHL_WHDWGL_Add1'))
    testunit.addTest(WHDW.test_WHDW_Add.MyTestCase_ZZHL_WHDWGL_Add('test_ZZHL_WHDWGL_Add2'))
    testunit.addTest(WHDW.test_WHDW_Look.MyTestCase_ZZHL_WHDWGL_Look('test_ZZHL_WHDWGL_Look'))
    testunit.addTest(WHDW.test_WHDW_Fwzz.MyTestCase_ZZHL_WHDWGL_Edit('test_ZZHL_AZTJFX_Edit1'))
    testunit.addTest(WHDW.test_WHDW_Fwzz.MyTestCase_ZZHL_WHDWGL_Edit('test_ZZHL_AZTJFX_Edit2'))
    testunit.addTest(WHDW.test_WHDW_Logout.MyTestCase_ZZHL_WHDWGL_Logout('test_ZZHL_WHDWGL_Logout1'))
    testunit.addTest(WHDW.test_WHDW_Logout.MyTestCase_ZZHL_WHDWGL_Logout('test_ZZHL_WHDWGL_Logout2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-维护单位管理模块-测试报告',
                  description='智慧护栏平台-维护单位管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../WHDW/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='安装统计分析模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)