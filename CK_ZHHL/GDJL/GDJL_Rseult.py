import base
import unittest
from BeautifulReport import BeautifulReport
import GDJL.test_GDJL_Cx
import GDJL.test_GDJL_JLDC
import GDJL.test_GDJL_Look
import GDJL.test_GDJL_Shenhe


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(GDJL.test_GDJL_Cx.MyTestCase_ZHHL_DbGD_Cx('test_ZHHL_DbGD_Cx'))
    testunit.addTest(GDJL.test_GDJL_Cx.MyTestCase_ZHHL_DbGD_Cx('test_ZHHL_DbGD_Fy'))
    testunit.addTest(GDJL.test_GDJL_JLDC.MyTestCase_ZHHL_DbGD_Dcsb('test_ZHHL_DbGD_Dcsb'))
    testunit.addTest(GDJL.test_GDJL_Look.MyTestCase_ZHHL_DbGD_Look('test_ZHHL_DbGD_Look'))
    testunit.addTest(GDJL.test_GDJL_Shenhe.MyTestCase_ZHHL_DbGD_Shenhe('test_ZHHL_DbGD_Shenhe'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-待办工单模块-测试报告',
                  description='智慧护栏平台-待办工单模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../Login/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='里程统计分析模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)