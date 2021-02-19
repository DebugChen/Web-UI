import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase_CLJK_Login(unittest.TestCase):
    '''车辆监控平台-登录模块-测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_CLJK\LOGIN\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\Login\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\KHXXGL\image1\KHXXGL_Add.png')
        # 关闭浏览器
        cls.dr.quit()

    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_Login')
    def test_CLJK_Login(self):
        '''登录模块-登录测试用例'''
        # 输入登录网址
        self.dr.get("https://ebeta.starlinkware.com/")
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 输入用户名
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("chenkai")
        # 输入密码
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("Xd0020110")
        # 输入验证码
        wait.until(EC.visibility_of_element_located((By.ID, "code"))).send_keys("1234")
        # 点击登录按钮
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@value="登录"]'))).click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        p = self.dr.find_element_by_xpath('//*[@id="deviceNum"]/div[1]/p').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '设备总数', '登录失败')
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_Exit')
    def test_CLJK_Exit(self):
        '''登录模块-登出测试用例'''
        wait1 = WebDriverWait(self.dr, 10, 0.2)
        # 点击退出登录
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//button[@title="退出登录"]'))).click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[4]/label/span[2]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '记住密码', '登出失败')
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_Login('test_CLJK_Login'))
    testunit.addTest(MyTestCase_CLJK_Login('test_CLJK_Exit'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-登录模块-登录登出测试报告',
                  description='车辆监控平台-登录模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 定义测试报告存放路径
    # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)