import base
import unittest
from BeautifulReport import BeautifulReport
import KHXXGL.test_KHXXGL_Cx
import KHXXGL.test_KHXXGL_Add
import KHXXGL.test_KHXXGL_Edit
import KHXXGL.test_KHXXGL_Look
import KHXXGL.test_KHXXGL_Logout
import KHXXGL.test_KHXXGL_Delete
import KHXXGL.test_KHXXGL_Khqy


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(KHXXGL.test_KHXXGL_Cx.MyTestCase_CLJK_KHXXGL_Cx('test_CLJK_KHXXGL_Cx'))
    testunit.addTest(KHXXGL.test_KHXXGL_Cx.MyTestCase_CLJK_KHXXGL_Cx('test_CLJK_KHXXGL_Fy'))
    testunit.addTest(KHXXGL.test_KHXXGL_Cx.MyTestCase_CLJK_KHXXGL_Cx('test_CLJK_KHZLGL_Khscx'))
    testunit.addTest(KHXXGL.test_KHXXGL_Add.MyTestCase_CLJK_KHXXGL_Add('test_CLJK_KHXXGL_Add1'))
    testunit.addTest(KHXXGL.test_KHXXGL_Add.MyTestCase_CLJK_KHXXGL_Add('test_CLJK_KHXXGL_Add2'))
    testunit.addTest(KHXXGL.test_KHXXGL_Edit.MyTestCase_CLJK_KHXXGL_Edit('test_CLJK_KHXXGL_Edit1'))
    testunit.addTest(KHXXGL.test_KHXXGL_Edit.MyTestCase_CLJK_KHXXGL_Edit('test_CLJK_KHXXGL_Edit2'))
    testunit.addTest(KHXXGL.test_KHXXGL_Look.MyTestCase_CLJK_KHXXGL_Look('test_CLJK_KHXXGL_Look'))
    testunit.addTest(KHXXGL.test_KHXXGL_Logout.MyTestCase_CLJK_KHXXGL_Logout('test_CLJK_KHXXGL_Logout1'))
    testunit.addTest(KHXXGL.test_KHXXGL_Logout.MyTestCase_CLJK_KHXXGL_Logout('test_CLJK_KHXXGL_Logout2'))
    testunit.addTest(KHXXGL.test_KHXXGL_Delete.MyTestCase_CLJK_KHXXGL_Delete('test_CLJK_KHXXGL_Delete1'))
    testunit.addTest(KHXXGL.test_KHXXGL_Delete.MyTestCase_CLJK_KHXXGL_Delete('test_CLJK_KHXXGL_Delete2'))
    testunit.addTest(KHXXGL.test_KHXXGL_Khqy.MyTestCase_CLJK_KHXXGL_Khqy('test_CLJK_KHXXGL_Khqy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-客户信息管理模块-测试报告',
                  description='车辆监控平台-客户信息管理模块-测试用例执行情况',
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