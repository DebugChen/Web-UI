import base
import unittest
from BeautifulReport import BeautifulReport
import QXGL.test_QXGL_Cx
import QXGL.test_QXGL_Add
import QXGL.test_QXGL_Edit
import QXGL.test_QXGL_Forbidden
import QXGL.test_QXGL_Cdqx


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(QXGL.test_QXGL_Cx.MyTestCase_ZHHL_JSQXGL_Cx('test_ZHHL_JSQXGL_Cx'))
    testunit.addTest(QXGL.test_QXGL_Cx.MyTestCase_ZHHL_JSQXGL_Cx('test_ZHHL_JSQXGL_Fy'))
    testunit.addTest(QXGL.test_QXGL_Add.MyTestCase_ZHHL_JSQXGL_Add('test_ZHHL_JSQXGL_Add1'))
    testunit.addTest(QXGL.test_QXGL_Add.MyTestCase_ZHHL_JSQXGL_Add('test_ZHHL_JSQXGL_Add2'))
    testunit.addTest(QXGL.test_QXGL_Edit.MyTestCase_ZHHL_JSQXGL_Edit('test_ZHHL_JSQXGL_Edit1'))
    testunit.addTest(QXGL.test_QXGL_Edit.MyTestCase_ZHHL_JSQXGL_Edit('test_ZHHL_JSQXGL_Edit2'))
    testunit.addTest(QXGL.test_QXGL_Forbidden.MyTestCase_ZHHL_JSQXGL_Forbidden('test_ZHHL_JSQXGL_Forbidden1'))
    testunit.addTest(QXGL.test_QXGL_Forbidden.MyTestCase_ZHHL_JSQXGL_Forbidden('test_ZHHL_JSQXGL_Forbidden2'))
    testunit.addTest(QXGL.test_QXGL_Cdqx.MyTestCase_ZHHL_JSQXGL_Cdqx('test_ZHHL_JSQXGL_Cdqx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-角色权限管理模块-测试报告',
                  description='智慧护栏平台-角色权限管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../Login/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='角色权限管理模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)