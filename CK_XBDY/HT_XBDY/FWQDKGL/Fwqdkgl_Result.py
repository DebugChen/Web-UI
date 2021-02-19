import base
import unittest
from BeautifulReport import BeautifulReport
import HT_XBDY.FWQDKGL.test_Fwqdkgl_Cx
import HT_XBDY.FWQDKGL.test_Fwqdkgl_Add
import HT_XBDY.FWQDKGL.test_Fwqdkgl_Edit
import HT_XBDY.FWQDKGL.test_Fwqdkgl_Delete
import HT_XBDY.FWQDKGL.test_Fwqdkgl_Pldelete


if __name__=='__main__':
    # 构造测试套件
    testunit=unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Cx.MyTestCase_XBDY_FWQDKGL_Cx('test_XBDY_FWQDKGL_Cx'))
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Cx.MyTestCase_XBDY_FWQDKGL_Cx('test_XBDY_FWQDKGL_Fy'))
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Add.MyTestCase_XBDY_FWQDKGL_Add('test_XBDY_FWQDKGL_Add'))
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Edit.MyTestCase_XBDY_FWQDKGL_Edit('test_XBDY_FWQDKGL_Edit1'))
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Edit.MyTestCase_XBDY_FWQDKGL_Edit('test_XBDY_FWQDKGL_Edit2'))
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Delete.MyTestCase_XBDY_FWQDKGL_Delete('test_XBDY_FWQDKGL_Delete'))
    testunit.addTest(HT_XBDY.FWQDKGL.test_Fwqdkgl_Pldelete.MyTestCase_XBDY_FWQDKGL_PlDelete('test_XBDY_FWQDKGL_PlDelete'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-服务器端口管理模块-测试报告',
                  description='新北斗云平台-服务器端口管理模块-测试用例执行情况',
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