import base
import unittest
from BeautifulReport import BeautifulReport
import GYSLB.test_Gyslb_Add
import GYSLB.test_Gyslb_Cx
import GYSLB.test_Gyslb_Delete
import GYSLB.test_Gyslb_Edit


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(GYSLB.test_Gyslb_Cx.MyTestCase_XBDY_GYSLB_Cx('test_XBDY_GYSLB_Cx'))
    testunit.addTest(GYSLB.test_Gyslb_Cx.MyTestCase_XBDY_GYSLB_Cx('test_XBDY_GYSLB_Fy'))
    testunit.addTest(GYSLB.test_Gyslb_Add.MyTestCase_XBDY_GYSLB_Add('test_XBDY_GYSLB_Add'))
    testunit.addTest(GYSLB.test_Gyslb_Edit.MyTestCase_XBDY_GYSLB_Edit('test_XBDY_GYSLB_Edit1'))
    testunit.addTest(GYSLB.test_Gyslb_Edit.MyTestCase_XBDY_GYSLB_Edit('test_XBDY_GYSLB_Edit2'))
    testunit.addTest(GYSLB.test_Gyslb_Delete.MyTestCase_XBDY_GYSLB_Delete('test_XBDY_GYSLB_Delete'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-供应商列表模块-测试报告',
                  description='新北斗云平台-供应商列表模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 运行用例filename=报告名称，
    # description=所有用例总的名称，
    # report_path=报告路径,如果不填写默认当前执行文件目录，
    # theme=报告的主题，有四种可以选择：theme_default，theme_cyan，theme_candy，theme_memories  默认是第一种

    # # 定义测试报告存放路径
    # fp=open('../LSTZ/image1/result2.html','wb')
    # # 定义测试报告
    # runner=HTMLTestRunner(stream=fp,title='车辆监控平台-UI自动化测试报告',description='客户信息管理模块-测试用例执行情况')
    # # 执行测试用例
    # runner.run(testunit)