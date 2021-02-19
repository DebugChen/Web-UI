import base
import unittest
from BeautifulReport import BeautifulReport
import WLSTJFX.test_WLSTJFX_Cx
import WLSTJFX.test_WLSTJFX_Look
import WLSTJFX.test_WLSTJFX_Sysjdc


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(WLSTJFX.test_WLSTJFX_Cx.MyTestCase_CLJK_WLSTJFX_Cx('test_CLJK_WLSTJFX_Cx'))
    testunit.addTest(WLSTJFX.test_WLSTJFX_Cx.MyTestCase_CLJK_WLSTJFX_Cx('test_CLJK_WLSTJFX_Fy'))
    testunit.addTest(WLSTJFX.test_WLSTJFX_Look.MyTestCase_CLJK_WLSTJFX_Look('test_CLJK_WLSTJFX_Look'))
    testunit.addTest(WLSTJFX.test_WLSTJFX_Look.MyTestCase_CLJK_WLSTJFX_Look('test_CLJK_WLSTJFX_Look_Fy'))
    testunit.addTest(WLSTJFX.test_WLSTJFX_Look.MyTestCase_CLJK_WLSTJFX_Look('test_CLJK_WLSTJFX_Look_Sjdc'))
    testunit.addTest(WLSTJFX.test_WLSTJFX_Look.MyTestCase_CLJK_WLSTJFX_Look('test_CLJK_WLSTJFX_Look_Gjzz'))
    testunit.addTest(WLSTJFX.test_WLSTJFX_Sysjdc.MyTestCase_CLJK_WLSTJFX_Sysjdc('test_CLJK_WLSTJFX_Sysjdc'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-物流锁统计分析模块-测试报告',
                  description='车辆监控平台-物流锁统计分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 运行用例filename=报告名称，
    # description=所有用例总的名称，
    # report_path=报告路径,如果不填写默认当前执行文件目录，
    # theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种

    # # 定义测试报告存放路径
    # fp=open('../KHXXGL/image1/result2.html','wb')
    # # 定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='客户信息管理模块-测试用例执行情况')
    # # 执行测试用例
    # runner.run(testunit)