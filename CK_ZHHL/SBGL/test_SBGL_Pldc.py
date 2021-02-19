import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_ZHHL_SBZLGL_Pldc(unittest.TestCase):
    '''智慧护栏平台-设备资料管理模块-批量导出测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\SBGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\SBZLGL\img"), img_name))

    @classmethod
    # 启动测试用例方法
    def setUpClass(cls):
        # # 启动Chrome浏览器
        # cls.dr=webdriver.Chrome()
        # # 最大化浏览器
        # cls.dr.maximize_window()
        # # 输入登录网址
        # cls.dr.get("https://railbeta.starlinkware.com/")
        # time.sleep(2)

        chromedriver = "D:\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "E:\自动化下载文件存放"}
        chromeOptions.add_experimental_option("prefs", prefs)
        cls.dr = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get('https://railbeta.starlinkware.com/')
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
        # 点击设备资料管理菜单
        cls.dr.find_element_by_xpath("/html/body/div[2]/ul/li[2]/ul/li").click()
        time.sleep(2)

    @classmethod
    # 关闭测试用例方法
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\untitled_CLJK\SBGL\image\SBZLGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_SBZLGL_Pldc')
    def test_ZHHL_SBZLGL_Pldc(self):
        '''设备资料管理模块-批量导出测试用例'''
        # 点击批量导出（导出所有）
        self.dr.find_element_by_xpath('//div[@class="btnArrList"]/button[4]').click()
        time.sleep(8)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_SBZLGL_Pldc('test_ZHHL_SBZLGL_Pldc'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-设备资料管理模块-批量导出测试报告',
                  description='智慧护栏平台-设备资料管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)