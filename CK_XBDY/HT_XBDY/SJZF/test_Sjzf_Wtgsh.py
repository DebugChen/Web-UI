import base
import os
from BeautifulReport import BeautifulReport
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_Sjzf_Wtgsh(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-数据转发模块-未通过审核测试集'''

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
    @BeautifulReport.add_test_img('test_XBDY_Sjzf_Wtgsh')
    def test_XBDY_Sjzf_Wtgsh(self):
        '''数据转发模块-未通过审核测试用例'''
        # self.dr = webdriver.Chrome()

        # 切换数据转发菜单
        self.dr.find_element_by_xpath('//div[@class="change"]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[3]/ul/li[2]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/ul/a[6]').click()
        time.sleep(2)

        # #按IMEI精确查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//div[@class="search-show"]/div[1]/div/div[1]/button').click()
        time.sleep(1)


if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_Sjzf_Wtgsh('test_XBDY_Sblb_Wtgsh'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-数据转发模块-未通过审核测试报告',
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