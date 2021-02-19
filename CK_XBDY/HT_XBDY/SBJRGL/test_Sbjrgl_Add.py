import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sbjrgl_Add(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备接入管理模块-接入设备测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\SBJRGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\SBJRGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sbjrgl_Add')
    def test_XBDY_Sbjrgl_Add(self):
        '''设备接入管理模块-接入设备测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换设备接入管理菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[1]').click()
        time.sleep(2)
        # self.dr.find_element_by_xpath('//div[@class="stretch"]').click()
        # time.sleep(2)

        # 点击接入设备
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[3]').click()
        time.sleep(1)
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入15位IMEI"]').send_keys('861097040963098')
        time.sleep(1)
        # 选择网络类型
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div'
            '/div[2]/div/form/div[1]/div[2]/div/div/div/div[1]/div').click()
        time.sleep(1)
        # 选中：内网
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-select ivu-select-visible ivu-select-single'
            ' ivu-select-default"]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 选择供应商
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div'
            '/div/div[2]/div/form/div[2]/div[1]/div/div/div/div[1]/div').click()
        time.sleep(1)
        # 选中：惠州博实结科技有限公司
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-select ivu-select-visible ivu-select-single'
            ' ivu-select-default"]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 选择供应商设备型号
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div'
            '/div[2]/div/form/div[2]/div[2]/div/div/div/div[1]/div').click()
        time.sleep(1)
        # 选中：C2608
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-select ivu-select-visible ivu-select-single'
            ' ivu-select-default"]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[3]/div/div/button[1]').click()
        time.sleep(1)
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI号"]').send_keys('861097040963098')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '861097040963098', '接入设备失败')
        time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sbjrgl_Add('test_XBDY_Sbjrgl_Add'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备接入管理模块-接入设备测试报告',
                  description='新北斗云平台-设备接入管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)