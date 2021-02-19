import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_WHDWGL_Add(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-维护单位模块-新增测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\WHDW\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\WHDWGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_WHDWGL_Add1')
    def test_ZHHL_WHDWGL_Add1(self):
        '''维护单位管理模块-新增测试用例'''
        # 鼠标悬停在“工单管理”链接上
        link = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/div/div[1]/li')
        ActionChains(self.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击维护单位菜单
        self.dr.find_element_by_xpath("//p[.='维护单位']").click()
        time.sleep(2)
        # 点击新增按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[3]/button').click()
        time.sleep(1)
        # 输入维护单位
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[1]/div/div/input').send_keys('测试维护单位01')
        time.sleep(1)
        # 选择服务组织
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[2]/div/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中新洲大队
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[2]/div/div/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        # 输入维护单位框
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul/li[1]/div/input')\
            .send_keys('测试维护单位01')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 定义变量，用于存放获取到的页面元素
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '测试维护单位01', '新增维护单位失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_WHDWGL_Add2')
    def test_ZHHL_WHDWGL_Add2(self):
        '''维护单位管理模块-新增测试用例'''
        # 点击新增按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[3]/button').click()
        time.sleep(1)
        # 输入维护单位
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[1]/div/div/input').send_keys('测试维护单位02')
        time.sleep(1)
        # 选择服务组织
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[2]/div/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中新洲大队
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[2]/div/div/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        # 输入维护单位框
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul/li[1]/div/input')\
            .send_keys('测试维护单位02')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 定义变量，用于存放获取到的页面元素
        span2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, '测试维护单位02', '新增维护单位失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_WHDWGL_Add('test_ZHHL_WHDWGL_Add1'))
    testunit.addTest(MyTestCase_ZHHL_WHDWGL_Add('test_ZHHL_WHDWGL_Add2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-维护单位模块-新增测试报告',
                  description='城市基础设施监测平台-维护单位模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)