import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sjzf_Cx(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-数据转发模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\SJZF\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'  .format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\SJZF\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sjzf_Cx')
    def test_XBDY_Sjzf_Cx(self):
        '''数据转发模块-查询测试用例'''
        self.dr = webdriver.Chrome()

        # 切换数据转发菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[6]').click()
        time.sleep(2)

        # #按工单ID精确查询
        # 选择查询条件：工单ID
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 输入工单ID
        self.dr.find_element_by_xpath(
            '//input[@placeholder="内容搜索"]').send_keys('1310046218364583936')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[2]/div'
            '/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div[2]/i[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '1310046218364583936', '按工单ID精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按工单ID模糊查询
        # 选择查询条件：工单ID
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 输入工单ID
        self.dr.find_element_by_xpath(
            '//input[@placeholder="内容搜索"]').send_keys('3936')
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[2]/div'
            '/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div[2]/i[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '1310046218364583936', '按工单ID模糊查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按创建时间查询
        # 选择查询条件：创建时间
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 选择时间段
        self.dr.find_element_by_xpath('//input[@placeholder="选择时间段"]').click()
        time.sleep(1)
        # 选择月份
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]'
            '/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/span[3]/span[2]').click()
        time.sleep(1)
        # 选中九月
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]'
            '/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/span[9]/em').click()
        time.sleep(1)
        # 选中九月24至25
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]'
            '/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/span[26]/em').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]'
            '/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/span[27]/em').click()
        time.sleep(1)
        # 点击确定
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]'
            '/div[1]/div[2]/div[2]/div/div/div/div[4]/button[3]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '2020-09-24 17:20:07', '按创建时间查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按创建人精确查询
        # 选择查询条件：创建人
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 输入创建人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="内容搜索"]').send_keys('个人用户')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[2]/i[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '个人用户', '按创建人精确查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按创建人模糊查询
        # 选择查询条件：创建人
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 输入创建人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="内容搜索"]').send_keys('个人')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[2]/i[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[3]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '个人用户', '按创建人模糊查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

        # #按审核状态查询
        # 选择查询条件：审核状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[1]/div/span').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]'
            '/div/div[1]/div[1]/div[1]/div[2]/ul[2]/li[4]').click()
        time.sleep(1)
        # 选择审核状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]').click()
        time.sleep(1)
        # 选中待审核
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div[2]/div[2]/ul[2]/li[1]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '待审核', '按审核状态查询失败')
        time.sleep(1)

        # 选择审核状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]').click()
        time.sleep(1)
        # 选中审核通过
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div[2]/div[2]/ul[2]/li[2]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '审核通过', '按审核状态查询失败')
        time.sleep(1)

        # 选择审核状态
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]').click()
        time.sleep(1)
        # 选中审核不通过
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[1]/div[1]/div[2]/div[2]/ul[2]/li[3]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//tbody[@class="ivu-table-tbody"]/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '审核不通过', '按审核状态查询失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Sjzf_Fy')
    def test_XBDY_Sjzf_Fy(self):
        '''数据转发模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中50条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(3)

        # #按100条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中100条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(3)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中20条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]'
            '/div[2]/div[2]/div/ul/div/div[1]/div/div[2]/ul[2]/li[1]').click()
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
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[3]/div[2]/div[2]/div/ul/div/div[2]/input').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div'
            '/div[3]/div[2]/div[2]/div/ul/div/div[2]/input').send_keys('4')
        time.sleep(1)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//ul[@class="ivu-page"]').click()
        time.sleep(2)
        # 点击清除
        self.dr.find_element_by_xpath('//div[@class="search-show"]/button[2]').click()
        time.sleep(3)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sjzf_Cx('test_XBDY_Sblb_Cx'))
    testunit.addTest(MyTestCase_XBDY_Sjzf_Cx('test_XBDY_Sblb_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-数据转发模块-查询测试报告',
                  description='新北斗云平台-数据转发模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)