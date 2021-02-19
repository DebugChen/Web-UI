import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_SBXHGL_Edit(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备型号管理模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\SBXHGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\SBXHGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_SBXHGL_Edit1')
    def test_XBDY_SBXHGL_Edit1(self):
        '''设备型号管理模块-编辑测试用例-新型号'''
        # self.dr = webdriver.Chrome()

        # 切换设备型号管理菜单
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[2]').click()
        time.sleep(2)

        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中供应商设备型号
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('测试型号S001')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr/td[7]/div/div/div/a[1]').click()
        time.sleep(1)
        # 选择供应商名称
        self.dr.find_element_by_xpath(
            '//div[@class="modal-list-content"]/div[1]/div[2]/div[1]/div/span').click()
        time.sleep(1)
        # 修改 惠州博实结科技有限公司
        self.dr.find_element_by_xpath(
            '//div[@class="modal-list-content"]/div[1]/div[2]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 修改供应商设备型号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入供应商设备型号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入供应商设备型号"]').send_keys('测试型号SS001')
        time.sleep(1)
        # 修改公司设备型号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入公司设备型号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入公司设备型号"]').send_keys('测试型号GG001')
        time.sleep(1)
        # 修改接入协议
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入接入协议"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入接入协议"]').send_keys('202')
        time.sleep(1)
        # 点击确认
        self.dr.find_element_by_xpath('//button[@class="ivu-btn ivu-btn-primary"]').click()
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中 供应商设备型号
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('测试型号SS001')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '测试型号SS001', '编辑设备型号失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_SBXHGL_Edit2')
    def test_XBDY_SBXHGL_Edit2(self):
        '''设备型号管理模块-编辑测试用例-旧型号'''
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中 供应商设备型号
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('测试型号SS001')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr/td[7]/div/div/div/a[1]').click()
        time.sleep(1)
        # 选择供应商名称
        self.dr.find_element_by_xpath(
            '//div[@class="modal-list-content"]/div[1]/div[2]/div[1]/div/span').click()
        time.sleep(1)
        # 修改 深圳市未智信息科技有限公司
        self.dr.find_element_by_xpath(
            '//div[@class="modal-list-content"]/div[1]/div[2]/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 修改供应商设备型号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入供应商设备型号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入供应商设备型号"]').send_keys('测试型号S001')
        time.sleep(1)
        # 修改公司设备型号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入公司设备型号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入公司设备型号"]').send_keys('测试型号G001')
        time.sleep(1)
        # 修改接入协议
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入接入协议"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入接入协议"]').send_keys('303')
        time.sleep(1)
        # 点击确认
        self.dr.find_element_by_xpath('//button[@class="ivu-btn ivu-btn-primary"]').click()
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)
        # 选择查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        # 选中 供应商设备型号
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('测试型号S001')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '测试型号S001', '编辑设备型号失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_SBXHGL_Edit('test_XBDY_SBXHGL_Edit1'))
    testunit.addTest(MyTestCase_XBDY_SBXHGL_Edit('test_XBDY_SBXHGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备型号管理模块-编辑测试报告',
                  description='新北斗云平台-设备型号管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)