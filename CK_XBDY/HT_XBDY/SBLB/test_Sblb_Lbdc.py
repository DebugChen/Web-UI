import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sblb_Lbdc(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备列表模块-列表导出测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\SBLB\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\SBLB\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sblb_Pldc')
    def test_XBDY_Sblb_Lbdc(self):
        '''设备列表模块-列表导出测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换设备列表菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[2]').click()
        time.sleep(2)

        # 勾选需要批量导出设备
        self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[1]/div/label/span/input').click()
        self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[2]/td[1]/div/label/span/input').click()
        time.sleep(1)
        # 点击批量导出
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[3]').click()
        time.sleep(5)

        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//div[@class="ivu-message-custom-content ivu-message-success"]/span').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '正在异步处理程序', '批量导出设备失败')
        # time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sblb_Lbdc('test_XBDY_Sblb_Lbdc'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备列表模块-列表导出测试报告',
                  description='新北斗云平台-设备列表模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)