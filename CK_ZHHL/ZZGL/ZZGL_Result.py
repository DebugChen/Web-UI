import base
import unittest
from BeautifulReport import BeautifulReport
import ZZGL.test_ZZGL_Cx
import ZZGL.test_ZZGL_Add
import ZZGL.test_ZZGL_Edit
import ZZGL.test_ZZGL_Logout
import ZZGL.test_ZZGL_Bddw


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(ZZGL.test_ZZGL_Cx.MyTestCase_ZHHL_KHXXGL_Cx('test_ZHHL_KHXXGL_Cx'))
    testunit.addTest(ZZGL.test_ZZGL_Cx.MyTestCase_ZHHL_KHXXGL_Cx('test_ZHHL_KHXXGL_Fy'))
    testunit.addTest(ZZGL.test_ZZGL_Cx.MyTestCase_ZHHL_KHXXGL_Cx('test_ZHHL_KHZLGL_Khscx'))
    testunit.addTest(ZZGL.test_ZZGL_Add.MyTestCase_ZHHL_KHXXGL_Add('test_ZHHL_KHXXGL_Add1'))
    testunit.addTest(ZZGL.test_ZZGL_Add.MyTestCase_ZHHL_KHXXGL_Add('test_ZHHL_KHXXGL_Add2'))
    testunit.addTest(ZZGL.test_ZZGL_Bddw.MyTestCase_ZHHL_KHXXGL_Bddw('test_ZHHL_KHXXGL_Bddw1'))
    testunit.addTest(ZZGL.test_ZZGL_Bddw.MyTestCase_ZHHL_KHXXGL_Bddw('test_ZHHL_KHXXGL_Bddw2'))
    testunit.addTest(ZZGL.test_ZZGL_Edit.MyTestCase_ZHHL_KHXXGL_Edit('test_ZHHL_KHXXGL_Edit1'))
    testunit.addTest(ZZGL.test_ZZGL_Edit.MyTestCase_ZHHL_KHXXGL_Edit('test_ZHHL_KHXXGL_Edit2'))
    testunit.addTest(ZZGL.test_ZZGL_Logout.MyTestCase_ZHHL_KHXXGL_Logout('test_ZHHL_KHXXGL_Logout1'))
    testunit.addTest(ZZGL.test_ZZGL_Logout.MyTestCase_ZHHL_KHXXGL_Logout('test_ZHHL_KHXXGL_Logout2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-客户信息管理模块-测试报告',
                  description='智慧护栏平台-客户信息管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 运行用例filename=报告名称，
    # description=所有用例总的名称，
    # report_path=报告路径,如果不填写默认当前执行文件目录，
    # theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种

    # # 定义测试报告存放路径
    # fp=open('../ZZGL/image1/result2.html','wb')
    # # 定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='客户信息管理模块-测试用例执行情况')
    # # 执行测试用例
    # runner.run(testunit)