import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_FWQDKGL_Delete(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-服务器端口管理模块-删除测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\FWQDKGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\FWQDKGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_FWQDKGL_Delete')
    def test_XBDY_FWQDKGL_Delete(self):
        '''服务器端口管理模块-删除测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换服务器端口管理菜单
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[3]').click()
        time.sleep(2)

        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中服务器IP（公网）
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('111.47.250.104')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 点击删除
        self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr/td[7]/div/div/div/a[2]').click()
        time.sleep(2)
        # 点击确认
        self.dr.find_element_by_xpath(
            '//div[@class="modal-footer"]/button[1]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-notice"]/div/div[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '删除成功', '删除服务器端口失败')
        time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_FWQDKGL_Delete('test_XBDY_FWQDKGL_Delete'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-服务器端口管理模块-删除测试报告',
                  description='新北斗云平台-服务器端口管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)