import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sblb_Xgsbz(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备列表模块-修改设备组测试集'''

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
    @BeautifulReport.add_test_img('test_XBDY_Sblb_Xzsbz')
    def test_XBDY_Sblb_Xzsbz(self):
        '''设备列表模块-修改设备组测试用例-新增'''
        # self.dr = webdriver.Chrome()

        # 切换设备列表菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[2]').click()
        time.sleep(2)

        # 点击下拉选项
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 切换自定义设备组项
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(1)

        # 点击修改设备组
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[2]/div[3]/div/div[1]/button').click()
        time.sleep(1)
        # 点击新增设备组
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]/div[1]/button').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-info"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '新增成功', '新增设备组失败')
        time.sleep(1)
        # 点击新增子设备组
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div[2]/ul[3]/li/span[2]/span/span/span[2]/button[1]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-info"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '新增成功', '新增子设备组失败')
        time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sblb_Xgsbz')
    def test_XBDY_Sblb_Xgsbz(self):
        '''设备列表模块-修改设备组测试用例-修改'''
        # self.dr = webdriver.Chrome()

        # 点击设备组名称
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div'
            '/div/div[2]/div[2]/ul[3]/li/span[2]/span/span').click()
        time.sleep(1)
        # 修改设备组名称
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div[2]/ul[3]/li/span[2]/span/span/input').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div[2]/ul[3]/li/span[2]/span/span/input').send_keys('测试设备组3')
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div[2]/ul[3]/li/span[2]/span/span/span[2]/button[1]').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap"]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-info"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '修改成功', '修改设备组失败')
        time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sblb_Scsbz')
    def test_XBDY_Sblb_Scsbz(self):
        '''设备列表模块-修改设备组测试用例-删除'''
        # self.dr = webdriver.Chrome()

        # 点击删除子设备组
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]'
            '/div[2]/ul[3]/li/ul/li/span[2]/span/span/span[2]/button[2]').click()
        time.sleep(1)
        # 点击删除父设备组
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[2]/div[2]/ul[3]/li/span[2]/span/span/span[2]/button[2]').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[3]/div/div/button[1]').click()
        time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sblb_Xgsbz('test_XBDY_Sblb_Xzsbz'))
    testunit.addTest(MyTestCase_XBDY_Sblb_Xgsbz('test_XBDY_Sblb_Xgsbz'))
    testunit.addTest(MyTestCase_XBDY_Sblb_Xgsbz('test_XBDY_Sblb_Scsbz'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备列表模块-修改设备组测试报告',
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