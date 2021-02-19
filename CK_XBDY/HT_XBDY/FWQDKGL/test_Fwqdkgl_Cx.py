import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_FWQDKGL_Cx(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-服务器端口管理模块-查询测试集'''

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
    @BeautifulReport.add_test_img('test_XBDY_FWQDKGL_Cx')
    def test_XBDY_FWQDKGL_Cx(self):
        '''服务器端口管理模块-查询测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换服务器端口管理菜单
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[3]').click()
        time.sleep(2)

        # #按设备接入协议类型精确查询
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中设备接入协议类型
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('102')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '102', '按设备接入协议类型精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

        # # #按设备接入协议类型模糊查询
        # # 选择查询条件
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        # time.sleep(1)
        # # 选中设备接入协议类型
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[1]').click()
        # time.sleep(1)
        # # 输入搜索内容
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="搜索内容"]').send_keys('2')
        # time.sleep(1)
        # # 点击查询
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '102', '按设备接入协议类型模糊查询失败')
        # time.sleep(1)
        # # 点击清除
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        # time.sleep(2)

        # #按服务器IP（公网）精确查询
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
            '//input[@placeholder="搜索内容"]').send_keys('111.47.250.101')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/label/span[1]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '111.47.250.101', '按服务器IP（公网）精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

        # # #按服务器IP（公网）模糊查询
        # # 选择查询条件
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        # time.sleep(1)
        # # 选中服务器IP（公网）
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[2]').click()
        # time.sleep(1)
        # # 输入搜索内容
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="搜索内容"]').send_keys('101')
        # time.sleep(1)
        # # 点击查询
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/label/span[1]').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '111.47.250.101', '按服务器IP（公网）模糊查询失败')
        # time.sleep(1)
        # # 点击清除
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        # time.sleep(2)

        # #按服务器端口号（公网）精确查询
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中服务器端口号（公网）
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('50003')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr/td[4]/div/label/span[1]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '50003', '按服务器端口号（公网）精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

        # # #按服务器端口号（公网）模糊查询
        # # 选择查询条件
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        # time.sleep(1)
        # # 选中服务器端口号（公网）
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[3]').click()
        # time.sleep(1)
        # # 输入搜索内容
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="搜索内容"]').send_keys('003')
        # time.sleep(1)
        # # 点击查询
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr/td[4]/div/label/span[1]').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '50003', '按服务器端口号（公网）模糊查询失败')
        # time.sleep(1)
        # # 点击清除
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        # time.sleep(2)

        # #按服务器IP(专网)精确查询
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中服务器IP(专网)
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[4]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('172.30.2.102')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/label/span[2]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '172.30.2.102', '按服务器IP(专网)精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

        # # #按服务器IP(专网)模糊查询
        # # 选择查询条件
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        # time.sleep(1)
        # # 选中服务器IP(专网)
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[4]').click()
        # time.sleep(1)
        # # 输入搜索内容
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="搜索内容"]').send_keys('102')
        # time.sleep(1)
        # # 点击查询
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/label/span[2]').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '172.30.2.102', '按服务器IP(专网)模糊查询失败')
        # time.sleep(1)
        # # 点击清除
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        # time.sleep(2)

        # #按服务器端口号(专网)精确查询
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中服务器端口号(专网)
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[5]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('60002')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]/div/label/span[2]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '60002', '按服务器端口号(专网)精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

        # # #按服务器端口号(专网)模糊查询
        # # 选择查询条件
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        # time.sleep(1)
        # # 选中服务器端口号(专网)
        # self.dr.find_element_by_xpath(
        #     '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[5]').click()
        # time.sleep(1)
        # # 输入搜索内容
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="搜索内容"]').send_keys('002')
        # time.sleep(1)
        # # 点击查询
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        # time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]/div/label/span[2]').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '60002', '按服务器端口号(专网)模糊查询失败')
        # time.sleep(1)
        # # 点击清除
        # self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        # time.sleep(2)

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_FWQDKGL_Fy')
    def test_XBDY_FWQDKGL_Fy(self):
        '''服务器端口管理模块-分页测试用例'''
        # #按40条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.DOWN)
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按40条分页显示）
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按80条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按80条分页显示）
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options"]/div[1]/div/div[1]/div/span').send_keys(Keys.ENTER)
        time.sleep(2)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//li[@title="下一页"]').click()
        time.sleep(2)
        # 点击上一页
        self.dr.find_element_by_xpath('//li[@title="上一页"]').click()
        time.sleep(2)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/ul/li[3]').click()
        time.sleep(2)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-elevator"]/input').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-elevator"]/input').send_keys('4')
        time.sleep(1)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//ul[@class="page-list ivu-page"]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_FWQDKGL_Cx('test_XBDY_FWQDKGL_Cx'))
    testunit.addTest(MyTestCase_XBDY_FWQDKGL_Cx('test_XBDY_FWQDKGL_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-服务器端口管理模块-查询测试报告',
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