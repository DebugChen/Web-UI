import base
import unittest
from BeautifulReport import BeautifulReport
import BJFX.test_BJFX_Cx
import BJFX.test_BJFX_Sjdc
import BJFX.test_BJFX_Dcbb
import BJFX.test_BJFX_Dcmx
import BJFX.test_BJFX_Lsbj
import BJFX.test_BJFX_Tqybj


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(BJFX.test_BJFX_Cx.MyTestCase_ZHHL_BJTJFX_Cx('test_ZHHL_BJTJFX_Cx'))
    testunit.addTest(BJFX.test_BJFX_Cx.MyTestCase_ZHHL_BJTJFX_Cx('test_ZHHL_BJTJFX_Fy'))
    testunit.addTest(BJFX.test_BJFX_Sjdc.MyTestCase_ZHHL_BJTJFX_Pldc('test_ZHHL_BJTJFX_Pldc'))
    testunit.addTest(BJFX.test_BJFX_Dcbb.MyTestCase_ZHHL_BJTJFX_Dcbb('test_ZHHL_BJTJFX_Dcbb'))
    testunit.addTest(BJFX.test_BJFX_Dcmx.MyTestCase_ZHHL_BJTJFX_Dcmx('test_ZHHL_BJTJFX_Dcmx'))
    testunit.addTest(BJFX.test_BJFX_Lsbj.MyTestCase_ZHHL_BJTJFX_Lsbj('test_ZHHL_BJTJFX_Lsbj'))
    testunit.addTest(BJFX.test_BJFX_Tqybj.MyTestCase_ZHHL_BJTJFX_Cjbjgd('test_ZHHL_BJTJFX_Cjbjgd'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-报警统计分析模块-测试报告',
                  description='智慧护栏平台-报警统计分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../BJFX/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='报警统计分析模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)