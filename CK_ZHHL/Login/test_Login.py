import os
from BeautifulReport import BeautifulReport
import time
import unittest
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_Login(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-登录模块-测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\Login\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\Login\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_Login')
    def test_ZHHL_Login(self):
        '''登录模块-登录测试用例'''
        # 获取查询结果，保存在变量里
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[3]/div[1]/div[1]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '设备统计', '登录失败')
        time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_Exit')
    def test_ZHHL_Exit(self):
        '''登录模块-登出测试用例'''
        # 点击退出登录按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/div/div/div[1]/img').click()
        time.sleep(1)
        # 获取查询结果，保存在变量里
        span2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[3]/div/div[1]/div[1]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, '账号登录', '登出失败')

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 执行测试用例
    testunit.addTest(MyTestCase_ZHHL_Login('test_ZHHL_Login'))
    testunit.addTest(MyTestCase_ZHHL_Login('test_ZHHL_Exit'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-登录模块-登录登出测试报告',
                  description='城市基础设施监测平台-登录模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp,
    #                           title='车辆监控平台UI自动化测试报告',
    #                           description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)