import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sbjrgl_Cx(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-设备接入管理模块-查询测试集'''

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
    @BeautifulReport.add_test_img('test_XBDY_Sbjrgl_Cx')
    def test_XBDY_Sbjrgl_Cx(self):
        '''设备接入管理模块-查询测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换设备接入管理菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[1]').click()
        time.sleep(2)

        # #按IMEI精确查询
        # 输入IMEi
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI号"]').send_keys('861097040963096')
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
        self.assertEqual(span, '861097040963096', '按IMEI精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按IMEI模糊查询
        # 输入IMEi
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI号"]').send_keys('3096')
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
        self.assertEqual(span, '861097040963096', '按IMEI模糊查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按接入时间精确查询
        # 选择接入时间
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择日期"]').click()
        time.sleep(1)
        # 选择月份
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-picker-panel-body"]/div[1]/span[3]/span[2]').click()
        time.sleep(1)
        # 选中九月
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-picker-panel-body"]/div[2]/div/span[9]/em').click()
        time.sleep(1)
        # 选择接入时间
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择日期"]').click()
        time.sleep(1)
        # 选中一日
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-picker-panel-body"]/div[2]/div/span[3]/em').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[2]/div/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[4]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '2020-09-01 00:00:00', '按接入时间精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按在线状态精确查询
        # 点击更多
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div[1]').click()
        time.sleep(1)
        # 选中在线状态查询条件
        self.dr.find_element_by_xpath('//input[@value="在线状态"]').click()
        time.sleep(1)
        # 点击在线状态查询条件
        self.dr.find_element_by_xpath(
            '//div[@style="display: inline; float: left;"]'
            '/div/button/span/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中在线状态：未注册
        self.dr.find_element_by_xpath(
            '//div[@style="display: inline; float: left;"]'
            '/div/button/span/div/div[2]/ul[2]/li[6]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[5]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '未注册', '按在线状态精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按版本号精确查询
        # 点击更多
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[3]/div[1]').click()
        time.sleep(1)
        # 选中版本号查询条件
        self.dr.find_element_by_xpath('//input[@value="版本号"]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//div[@class="pageName"]').click()
        time.sleep(1)
        # 点击版本号查询条件
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        # 输入版本号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入版本号"]').send_keys('123')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-wrapper"]/div[2]/div[2]/div'
            '/div[2]/div/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[1]').click()
        time.sleep(2)
        # # 获取页面元素，保存到变量
        # span = self.dr.find_element_by_xpath(
        #     '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]/div/span').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(span, '123', '按版本号精确查询失败')
        # time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # 按供应商名称精确查询
        # 点击左侧对应供应商：深圳市芯盛智能有限公司
        self.dr.find_element_by_xpath(
            '//div[@class="devices-list-tree"]/div/ul[5]/li/span[2]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath('//div[@class="ivu-table-cell-slot"]/button[1]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]/div/div/div[2]'
            '/div/form/div[2]/div[1]/div/div/div/div[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '深圳市芯盛智能有限公司', '按供应商名称精确查询失败')
        time.sleep(1)
        # 点击取消
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal"]'
            '/div/div/div[3]/div/div/button[2]').click()
        time.sleep(2)

        # 按供应商设备型号精确查询
        # 点击左侧对应供应商设备型号：C2608
        self.dr.find_element_by_xpath(
            '//div[@class="devices-list-tree"]/div/ul[5]/li/ul[1]/li/span[2]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, 'C2608', '按供应商设备型号精确查询失败')
        time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sbjrgl_Fy')
    def test_XBDY_Sbjrgl_Fy(self):
        '''设备接入管理模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//span[@class="ivu-select-selected-value"]').click()
        time.sleep(1)
        # 选中50条/页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-sizer"]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(3)

        # #按100条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//span[@class="ivu-select-selected-value"]').click()
        time.sleep(1)
        # 选中100条/页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-sizer"]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(3)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//span[@class="ivu-select-selected-value"]').click()
        time.sleep(1)
        # 选中20条/页
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-sizer"]/div/div[2]/ul[2]/li[1]').click()
        time.sleep(3)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//li[@title="下一页"]').click()
        time.sleep(3)
        # 点击上一页
        self.dr.find_element_by_xpath('//li[@title="上一页"]').click()
        time.sleep(3)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath('//li[@title="3"]').click()
        time.sleep(3)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-elevator"]/input').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-page-options-elevator"]/input').send_keys('4')
        time.sleep(3)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//ul[@class="ivu-page"]').click()
        time.sleep(3)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sbjrgl_Cx('test_XBDY_Sbjrgl_Cx'))
    testunit.addTest(MyTestCase_XBDY_Sbjrgl_Cx('test_XBDY_Sbjrgl_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-设备接入管理模块-查询测试报告',
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