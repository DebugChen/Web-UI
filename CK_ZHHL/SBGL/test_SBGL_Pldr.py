import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_ZHHL_SBZLGL_Pldr(unittest.TestCase):
    '''智慧护栏平台-设备资料管理模块-批量导入测试集'''

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

    # 执行文件上传方法
    @staticmethod
    def upload_file(exe, browser, filename):
        """
        使用autoIt上传文件
        :param exe: 上传文件的exe程序所在目录
        :param browser: 浏览器类型： firefox chrome ie
        :param filename: 待上传文件路径
        :return: none
        """
        cmd = exe + ' ' + browser + ' ' + filename
        os.system(cmd)

    @classmethod
    # 启动测试用例方法
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
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
        # 点击设备资料管理菜单
        cls.dr.find_element_by_xpath("/html/body/div[2]/ul/li[2]/ul/li").click()
        time.sleep(2)

    @classmethod
    # 关闭测试用例方法
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_SBZLGL_Pldr')
    def test_ZHHL_SBZLGL_Pldr(self):
        '''设备资料管理模块-批量导入测试用例'''
        # 点击批量导入
        self.dr.find_element_by_xpath('//div[@class="btnArrList"]/button[3]').click()
        time.sleep(1)
        # 点击选取文件弹出上传文件窗口
        upload_element = self.dr.find_element_by_xpath(
            '//div[@class="upload-demo"]/div[1]/button')
        action = ActionChains(self.dr)
        action.move_to_element(upload_element).click().perform()
        action.release()
        time.sleep(3)
        # 选取要上传的文件
        MyTestCase_ZHHL_SBZLGL_Pldr.upload_file(
            r'E:\123.exe ', 'chrome', r'E:\自动化下载文件存放\智慧护栏_设备导入模板.xlsx')
        time.sleep(2)
        # 点击上传文件
        self.dr.find_element_by_xpath('//div[@class="upload-demo"]/button').click()
        time.sleep(2)

        # 点击关闭
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[5]/div/div[2]/div[3]/div/button').click()
        time.sleep(1)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_SBZLGL_Pldr('test_ZHHL_SBZLGL_Pldr'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-设备资料管理模块-批量导入测试报告',
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