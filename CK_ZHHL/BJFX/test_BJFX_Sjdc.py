import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_ZHHL_BJFX_Pldc(unittest.TestCase):
    '''城市基础设施监测平台-报警分析模块-数据导出测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\BJFX\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\BJFX\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # # 启动Chrome浏览器
        # cls.dr = webdriver.Chrome()
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
        cls.dr.get("http://172.30.1.200:7070/")
        # 输入用户名
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys("chenkai")
        time.sleep(0.5)
        # 输入密码
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("Xd0020110")
        time.sleep(0.5)
        # 输入验证码
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys("1111")
        time.sleep(0.5)
        # 点击登录按钮
        cls.dr.find_element_by_class_name('loginEvent').click()
        time.sleep(2)
        # 鼠标悬停在“数据中心”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[1]/li')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 点击报警分析菜单
        cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[2]/div/div[2]/div/p').click()
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Pldc')
    def test_ZHHL_BJFX_Pldc(self):
        '''报警分析模块-数据导出测试用例'''
        # 点击数据导出
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[3]/button').click()
        time.sleep(1)
        # 点击生成报表并导出
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border'
            ' alarm-analysis data-export"]''/div/div/div[3]/div/div[2]/button').click()
        time.sleep(5)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_BJFX_Pldc('test_ZHHL_BJFX_Pldc'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-报警分析模块-数据导出测试报告',
                  description='城市基础设施监测平台-报警分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)