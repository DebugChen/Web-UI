import base
import unittest
from BeautifulReport import BeautifulReport
import SBGL.test_SBGL_Cx
import SBGL.test_SBGL_Add
import SBGL.test_SBGL_Edit
import SBGL.test_SBGL_Dismantle
import SBGL.test_SBGL_Look
import SBGL.test_SBGL_Mbxz
import SBGL.test_SBGL_Pldc


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(SBGL.test_SBGL_Cx.MyTestCase_ZHHL_SBZLGL_Cx('test_ZHHL_SBZLGL_Cx'))
    testunit.addTest(SBGL.test_SBGL_Cx.MyTestCase_ZHHL_SBZLGL_Cx('test_ZHHL_SBZLGL_Fy'))
    testunit.addTest(SBGL.test_SBGL_Cx.MyTestCase_ZHHL_SBZLGL_Cx('test_ZHHL_SBZLGL_Khscx'))
    testunit.addTest(SBGL.test_SBGL_Add.MyTestCase_ZHHL_SBZLGL_Add('test_ZHHL_SBZLGL_Add'))
    testunit.addTest(SBGL.test_SBGL_Mbxz.MyTestCase_ZHHL_SBZLGL_Mbxz('test_ZHHL_SBZLGL_Mbxz'))
    testunit.addTest(SBGL.test_SBGL_Pldc.MyTestCase_ZHHL_SBZLGL_Pldc('test_ZHHL_SBZLGL_Pldc'))
    testunit.addTest(SBGL.test_SBGL_Look.MyTestCase_ZHHL_SBZLGL_Look('test_ZHHL_SBZLGL_Look'))
    testunit.addTest(SBGL.test_SBGL_Edit.MyTestCase_ZHHL_SBZLGL_Edit('test_ZHHL_SBZLGL_Edit1'))
    testunit.addTest(SBGL.test_SBGL_Edit.MyTestCase_ZHHL_SBZLGL_Edit('test_ZHHL_SBZLGL_Edit2'))
    testunit.addTest(SBGL.test_SBGL_Dismantle.MyTestCase_ZHHL_SBZLGL_Dismantle('test_ZHHL_SBZLGL_Dismantle1'))
    testunit.addTest(SBGL.test_SBGL_Dismantle.MyTestCase_ZHHL_SBZLGL_Dismantle('test_ZHHL_SBZLGL_Dismantle2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-设备资料管理模块-测试报告',
                  description='智慧护栏平台-设备资料管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../SBGL/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='设备资料管理模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)
