import base
import unittest
from BeautifulReport import BeautifulReport
import SBZLGL.test_SBZLGL_Cx
import SBZLGL.test_SBZLGL_Add
import SBZLGL.test_SBZLGL_Delete
import SBZLGL.test_SBZLGL_Edit
import SBZLGL.test_SBZLGL_Dismantle
import SBZLGL.test_SBZLGL_Look
import SBZLGL.test_SBZLGL_Mbxz
import SBZLGL.test_SBZLGL_Pldc
import SBZLGL.test_SBZLGL_Pldr
import SBZLGL.test_SBZLGL_Plgx


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(SBZLGL.test_SBZLGL_Cx.MyTestCase_CLJK_SBZLGL_Cx('test_CLJK_SBZLGL_Cx'))
    testunit.addTest(SBZLGL.test_SBZLGL_Cx.MyTestCase_CLJK_SBZLGL_Cx('test_CLJK_SBZLGL_Fyxs'))
    testunit.addTest(SBZLGL.test_SBZLGL_Cx.MyTestCase_CLJK_SBZLGL_Cx('test_CLJK_SBZLGL_Khscx'))
    testunit.addTest(SBZLGL.test_SBZLGL_Add.MyTestCase_CLJK_SBZLGL_Add('test_CLJK_SBZLGL_Add'))
    testunit.addTest(SBZLGL.test_SBZLGL_Look.MyTestCase_CLJK_SBZLGL_Look('test_CLJK_SBZLGL_Look'))
    testunit.addTest(SBZLGL.test_SBZLGL_Edit.MyTestCase_CLJK_SBZLGL_Edit('test_CLJK_SBZLGL_Edit1'))
    testunit.addTest(SBZLGL.test_SBZLGL_Edit.MyTestCase_CLJK_SBZLGL_Edit('test_CLJK_SBZLGL_Edit2'))
    testunit.addTest(SBZLGL.test_SBZLGL_Delete.MyTestCase_CLJK_SBZLGL_Delete('test_CLJK_SBZLGL_Delete'))
    testunit.addTest(SBZLGL.test_SBZLGL_Dismantle.MyTestCase_CLJK_SBZLGL_Dismantle('test_CLJK_SBZLGL_Dismantle1'))
    testunit.addTest(SBZLGL.test_SBZLGL_Dismantle.MyTestCase_CLJK_SBZLGL_Dismantle('test_CLJK_SBZLGL_Dismantle2'))
    testunit.addTest(SBZLGL.test_SBZLGL_Mbxz.MyTestCase_CLJK_SBZLGL_Mbxz('test_CLJK_SBZLGL_Mbxz'))
    testunit.addTest(SBZLGL.test_SBZLGL_Pldc.MyTestCase_CLJK_SBZLGL_Pldc('test_CLJK_SBZLGL_Pldc'))
    testunit.addTest(SBZLGL.test_SBZLGL_Pldr.MyTestCase_CLJK_SBZLGL_Pldr('test_CLJK_SBZLGL_Pldr'))
    testunit.addTest(SBZLGL.test_SBZLGL_Plgx.MyTestCase_CLJK_SBZLGL_Plgx('test_CLJK_SBZLGL_Plgx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-设备资料管理模块-测试报告',
                  description='车辆监控平台-设备资料管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../SBZLGL/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='设备资料管理模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)
