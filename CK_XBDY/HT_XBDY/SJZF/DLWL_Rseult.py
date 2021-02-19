import unittest
from BeautifulReport import BeautifulReport
import SJZF.test_DLWL_Add
import SJZF.test_DLWL_Bd
import SJZF.test_DLWL_Delete
import SJZF.test_DLWL_Edit
import SJZF.test_DLWL_Jb


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(SJZF.test_DLWL_Add.MyTestCase_CLJK_DLWL_Add('test_CLJK_DLWL_Add'))
    testunit.addTest(SJZF.test_DLWL_Bd.MyTestCase_CLJK_DLWL_Bd('test_CLJK_DLWL_Bd'))
    testunit.addTest(SJZF.test_DLWL_Delete.MyTestCase_CLJK_DLWL_Delete('test_CLJK_DLWL_Delete'))
    testunit.addTest(SJZF.test_DLWL_Edit.MyTestCase_CLJK_DLWL_Edit('test_CLJK_DLWL_Edit'))
    testunit.addTest(SJZF.test_DLWL_Jb.MyTestCase_CLJK_DLWL_Jb('test_CLJK_DLWL_Jb'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-地理围栏模块-测试报告',
                  description='车辆监控平台-地理围栏模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../Login/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='地理围栏模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)