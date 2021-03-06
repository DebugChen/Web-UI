import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_ZHHL_AZXLGL_Szazbz(unittest.TestCase):
    '''智慧护栏平台-安装线路管理模块-设备安装标准测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\XLGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\AZXLGL\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://railbeta.starlinkware.com/")
        time.sleep(2)
        # 输入用户名
        cls.dr.find_element_by_id("username").send_keys("adminCK")
        time.sleep(1)
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Douniu2918")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击安装线路管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[5]/ul/li').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_AZXLGL_Szazbz1')
    def test_ZHHL_AZXLGL_Szazbz1(self):
        '''安装线路管理模块-设置安装标准测试用例-设置后'''
        # 点击设置安装标准按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[2]/button').click()
        time.sleep(2)
        # 输入限制数字
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[4]/div/div[2]/div/div[2]/div/input').clear()
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[4]/div/div[2]/div/div[2]/div/input').send_keys('20')
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[4]/div/div[3]/span/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        p = self.dr.find_element_by_xpath('//p[@class="el-message__content"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '设置成功', '设备安装标准失败')
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_AZXLGL_Szazbz2')
    def test_ZHHL_AZXLGL_Szazbz2(self):
        '''安装线路管理模块-设置安装标准测试用例-设置前'''
        # 点击设置安装标准按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[1]/div[2]/button').click()
        time.sleep(2)
        # 输入限制数字
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[4]/div/div[2]/div/div[2]/div/input').clear()
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[4]/div/div[2]/div/div[2]/div/input').send_keys('100')
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[4]/div/div[3]/span/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        p = self.dr.find_element_by_xpath('//p[@class="el-message__content"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '设置成功', '设备安装标准失败')
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_AZXLGL_Szazbz('test_ZHHL_AZXLGL_Szazbz1'))
    testunit.addTest(MyTestCase_ZHHL_AZXLGL_Szazbz('test_ZHHL_AZXLGL_Szazbz2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-安装线路管理模块-设置安装标准测试报告',
                  description='智慧护栏平台-安装线路管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../XLGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)