import unittest
from BeautifulReport import BeautifulReport
import JSTZ.test_JSQXGL_Cx
import JSTZ.test_JSQXGL_Add
import JSTZ.test_JSQXGL_Edit
import JSTZ.test_JSQXGL_Forbidden
import JSTZ.test_JSQXGL_Qx


if __name__=='__main__':
    # 组装测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(JSTZ.test_JSQXGL_Cx.MyTestCase_CLJK_JSQXGL_Cx('test_CLJK_JSQXGL_Cx'))
    testunit.addTest(JSTZ.test_JSQXGL_Cx.MyTestCase_CLJK_JSQXGL_Cx('test_CLJK_JSQXGL_Fy'))
    testunit.addTest(JSTZ.test_JSQXGL_Add.MyTestCase_CLJK_JSQXGL_Add('test_CLJK_JSQXGL_Add1'))
    testunit.addTest(JSTZ.test_JSQXGL_Add.MyTestCase_CLJK_JSQXGL_Add('test_CLJK_JSQXGL_Add2'))
    testunit.addTest(JSTZ.test_JSQXGL_Edit.MyTestCase_CLJK_JSQXGL_Edit('test_CLJK_JSQXGL_Edit1'))
    testunit.addTest(JSTZ.test_JSQXGL_Edit.MyTestCase_CLJK_JSQXGL_Edit('test_CLJK_JSQXGL_Edit2'))
    testunit.addTest(JSTZ.test_JSQXGL_Forbidden.MyTestCase_CLJK_JSQXGL_Forbidden('test_CLJK_JSQXGL_Forbidden'))
    testunit.addTest(JSTZ.test_JSQXGL_Qx.MyTestCase_CLJK_JSQXGL_Qx('test_CLJK_JSQXGL_Qx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-角色权限管理模块-测试报告',
                  description='车辆监控平台-角色权限管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # #定义测试报告存放路径
    # fp=open('../Login/image1/result1.html','wb')
    # #定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='角色权限管理模块-测试用例执行情况')
    # #执行测试用例
    # runner.run(testunit)