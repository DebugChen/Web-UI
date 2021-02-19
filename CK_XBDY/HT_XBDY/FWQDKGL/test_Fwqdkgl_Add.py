import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_FWQDKGL_Add(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-服务器端口管理模块-新增测试集'''

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
    @BeautifulReport.add_test_img('test_XBDY_FWQDKGL_Add')
    def test_XBDY_FWQDKGL_Add(self):
        '''服务器端口管理模块-新增测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换服务器端口管理菜单
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[3]').click()
        time.sleep(2)

        # 点击新增
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/button[1]').click()
        time.sleep(1)
        # 输入设备接入协议类型
        self.dr.find_element_by_xpath(
            '//input[@placeholder="输入设备接入协议类型"]').send_keys('104')
        time.sleep(1)
        # 输入服务器IP（公网）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="输入公网服务器IP"]').send_keys('111.47.250.104')
        time.sleep(1)
        # 输入服务器端口号（公网）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="输入公网服务器端口号"]').send_keys('50004')
        time.sleep(1)
        # 输入服务器IP（专网）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="输入专网服务器IP"]').send_keys('172.30.2.104')
        time.sleep(1)
        # 输入服务器端口号（专网）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="输入专网服务器端口号"]').send_keys('60004')
        time.sleep(1)
        # 点击确认
        self.dr.find_element_by_xpath('//button[@class="ivu-btn ivu-btn-primary"]').click()
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
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/label/span[1]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '111.47.250.104', '新增服务器端口失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_FWQDKGL_Add('test_XBDY_FWQDKGL_Add'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-服务器端口管理模块-新增测试报告',
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