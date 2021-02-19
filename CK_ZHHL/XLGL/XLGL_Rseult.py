import base
import unittest
from BeautifulReport import BeautifulReport
import XLGL.test_XLGL_Cx
import XLGL.test_XLGL_Szazbz
import XLGL.test_XLGL_Ckysh
import XLGL.test_XLGL_Dcazsb
import XLGL.test_XLGL_Cxld


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(XLGL.test_XLGL_Cx.MyTestCase_ZHHL_AZXLGL_Cx('test_ZHHL_AZXLGL_Cx'))
    testunit.addTest(XLGL.test_XLGL_Cx.MyTestCase_ZHHL_AZXLGL_Cx('test_ZHHL_AZXLGL_Fy'))
    testunit.addTest(XLGL.test_XLGL_Szazbz.MyTestCase_ZHHL_AZXLGL_Szazbz('test_ZHHL_AZXLGL_Szazbz'))
    testunit.addTest(XLGL.test_XLGL_Ckysh.MyTestCase_ZHHL_AZXLGL_Ckysh('test_ZHHL_AZXLGL_Ckysh'))
    testunit.addTest(XLGL.test_XLGL_Dcazsb.MyTestCase_ZHHL_AZXLGL_Dcazsb('test_ZHHL_AZXLGL_Dcazsb'))
    testunit.addTest(XLGL.test_XLGL_Cxld.MyTestCase_ZHHL_AZXLGL_Cxld('test_ZHHL_AZXLGL_Cxld'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-安装线路管理模块-测试报告',
                  description='智慧护栏平台-安装线路管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../BJFX/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='报警统计分析模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)