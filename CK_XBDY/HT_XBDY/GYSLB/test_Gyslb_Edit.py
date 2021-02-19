import base
import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_GYSLB_Edit(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-供应商列表模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\GYSLB\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\GYSLB\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_GYSLB_Edit1')
    def test_XBDY_GYSLB_Edit1(self):
        '''供应商列表模块-编辑测试用例'''
        # self.dr = webdriver.Chrome()

        # 选择查询条件
        self.dr.find_element_by_xpath('//span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中供应商名称
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('测试供应商02')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(1)
        # 点击编辑
        self.dr.find_element_by_xpath('//div[@class="table-operate"]/a[1]').click()
        time.sleep(1)
        # # 修改供应商名称
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="请输入供应商名称"]').send_keys('测试供应商022')
        # time.sleep(1)
        # 修改联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('测试供应商022')
        time.sleep(1)
        # 修改手机号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入手机号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入手机号"]').send_keys('1336542222')
        time.sleep(1)
        # 修改地址
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入地址"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入地址"]').send_keys('武汉市硚口区')
        time.sleep(1)
        # 点击确认
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap"]/div/div/div[3]/div/button[1]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-table-body"]/table/tbody/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '测试供应商022', '编辑供应商失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_GYSLB_Edit2')
    def test_XBDY_GYSLB_Edit2(self):
        '''供应商列表模块-编辑测试用例'''
        # 选择查询条件
        self.dr.find_element_by_xpath('//span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中供应商名称
        self.dr.find_element_by_xpath(
            '//div[@class="operate-details"]/div[1]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 输入搜索内容
        self.dr.find_element_by_xpath(
            '//input[@placeholder="搜索内容"]').send_keys('测试供应商02')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/div[2]/i').click()
        time.sleep(1)
        # 点击编辑
        self.dr.find_element_by_xpath('//div[@class="table-operate"]/a[1]').click()
        time.sleep(1)
        # # 修改供应商名称
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="请输入供应商名称"]').send_keys('测试供应商02')
        # time.sleep(1)
        # 修改联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('测试供应商02')
        time.sleep(1)
        # 修改手机号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入手机号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入手机号"]').send_keys('1336542111')
        time.sleep(1)
        # 修改地址
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入地址"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入地址"]').send_keys('武汉市')
        time.sleep(1)
        # 点击确认
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap"]/div/div/div[3]/div/button[1]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-table-body"]/table/tbody/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '测试供应商02', '编辑供应商失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="operate-details"]/button[2]').click()
        time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_GYSLB_Edit('test_XBDY_GYSLB_Edit1'))
    testunit.addTest(MyTestCase_XBDY_GYSLB_Edit('test_XBDY_GYSLB_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-供应商列表模块-编辑测试报告',
                  description='新北斗云平台-供应商列表模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)