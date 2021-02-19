import os
from BeautifulReport import BeautifulReport
import time
import unittest
from selenium.webdriver import ActionChains
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_GDJL_Look(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-工单记录模块-查看测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\GDJL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\GDJL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_GDJL_Look')
    def test_ZHHL_GDJL_Look(self):
        '''工单记录模块-查看测试用例'''
        # 鼠标悬停在“工单管理”链接上
        link = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/div/div[1]/li')
        ActionChains(self.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击工单记录菜单
        self.dr.find_element_by_xpath("//p[.='工单记录']").click()
        time.sleep(2)
        # 点击查看按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[8]/div/div/button').click()
        time.sleep(3)
        # 获取查询结果，保存在变量里
        div1 = self.dr.find_element_by_xpath(
            '//div[@class="contain-right"]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '维护记录', '查看失败')
        time.sleep(2)
        # 点击关闭窗口
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border see-order"]'
            '/div/div/div[1]/div/img').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_GDJL_Look('test_ZHHL_GDJL_Look'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-工单记录模块-查看测试报告',
                  description='城市基础设施监测平台-工单记录模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)