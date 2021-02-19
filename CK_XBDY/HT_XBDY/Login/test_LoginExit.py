import base
import os
from BeautifulReport import BeautifulReport
import time
import unittest
from test_Login_GG import MyTestCase_XBDY_Login_GG


class MyTestCase_XBDY_LoginExit(MyTestCase_XBDY_Login_GG):
    '''新北斗云平台-登录模块-测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_XBDY\HT_XBDY\Login\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_XBDY\HT_XBDY\Login\img"), img_name))

    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Login')
    def test_XBDY_Login(self):
        '''登录模块-登录测试用例'''
        # 点击收起左侧菜单
        self.dr.find_element_by_xpath('//div[@class="stretch"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[3]/div[2]/span[1]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '服务热线：027-83980088', '登录失败')
        time.sleep(2)

    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_XBDY_Exit')
    def test_XBDY_Exit(self):
        '''登录模块-登出测试用例'''
        # 点击头像
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div[2]/div[2]/img').click()
        time.sleep(1)
        # 点击退出
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[4]/ul/li[2]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/h2').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '欢迎登录北斗云平台', '登出失败')
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_XBDY_LoginExit('test_XBDY_Login'))
    testunit.addTest(MyTestCase_XBDY_LoginExit('test_XBDY_Exit'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='新北斗云平台-登录模块-登录登出测试报告',
                  description='新北斗云平台-登录模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 定义测试报告存放路径
    # fp = open('../LSTZ/image1/result2.html', 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)