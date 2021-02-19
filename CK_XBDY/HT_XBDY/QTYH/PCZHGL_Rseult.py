import unittest
from BeautifulReport import BeautifulReport
import QTYH.test_PCZHGL_Cx
import QTYH.test_PCZHGL_Add
import QTYH.test_PCZHGL_Edit
import QTYH.test_PCZHGL_Cshmi
import QTYH.test_PCZHGL_Logout
import QTYH.test_PCZHGL_Look
import QTYH.test_PCZHGL_Pldelete


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(QTYH.test_PCZHGL_Cx.MyTestCase_CLJK_PCZHGL_Cx('test_CLJK_PCZHGL_Cx'))
    testunit.addTest(QTYH.test_PCZHGL_Cx.MyTestCase_CLJK_PCZHGL_Cx('test_CLJK_PCZHGL_Fy'))
    testunit.addTest(QTYH.test_PCZHGL_Add.MyTestCase_CLJK_PCZHGL_Add('test_CLJK_PCZHGL_Add1'))
    testunit.addTest(QTYH.test_PCZHGL_Add.MyTestCase_CLJK_PCZHGL_Add('test_CLJK_PCZHGL_Add2'))
    testunit.addTest(QTYH.test_PCZHGL_Edit.MyTestCase_CLJK_PCZHGL_Edit('test_CLJK_PCZHGL_Edit1'))
    testunit.addTest(QTYH.test_PCZHGL_Edit.MyTestCase_CLJK_PCZHGL_Edit('test_CLJK_PCZHGL_Edit2'))
    testunit.addTest(QTYH.test_PCZHGL_Cshmi.MyTestCase_CLJK_PCZHGL_Cshmi('test_CLJK_PCZHGL_Cshmi'))
    testunit.addTest(QTYH.test_PCZHGL_Logout.MyTestCase_CLJK_PCZHGL_Logout('test_CLJK_PCZHGL_Logout'))
    testunit.addTest(QTYH.test_PCZHGL_Look.MyTestCase_CLJK_PCZHGL_Look('test_CLJK_PCZHGL_Look'))
    testunit.addTest(QTYH.test_PCZHGL_Pldelete.MyTestCase_CLJK_PCZHGL_Pldelete('test_CLJK_PCZHGL_Pldelete'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-PC账户管理模块-测试报告',
                  description='车辆监控平台-PC账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../Login/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='PC账户管理模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)