import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase_ZHHL_BJFX_TyQybj(unittest.TestCase):
    '''城市基础设施监测平台-报警分析模块-停用/启用报警测试集'''

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
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("http://172.30.1.200:7070/")
        wait = WebDriverWait(cls.dr, 10, 0.2)
        # 输入用户名
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入账号"]'))).send_keys("chenkai")
        # cls.dr.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys("chenkai")
        # time.sleep(0.5)
        # 输入密码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入密码"]'))).send_keys("Xd0020110")
        # cls.dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("Xd0020110")
        # time.sleep(0.5)
        # 输入验证码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入验证码"]'))).send_keys("1111")
        # cls.dr.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys("1111")
        # time.sleep(0.5)
        # 点击登录按钮
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'loginEvent'))).click()
        # cls.dr.find_element_by_class_name('loginEvent').click()
        # time.sleep(2)
        # 鼠标悬停在“数据中心”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[1]/li')))

        # link = cls.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[1]/li')
        ActionChains(cls.dr).move_to_element(link).perform()
        # time.sleep(1)
        # 点击报警分析菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[2]/div/div[2]/div/p'))).click()
        # cls.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[2]/div/div[2]/div/p').click()
        # time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Tybj')
    def test_ZHHL_BJFX_Tybj(self):
        '''报警分析模块-停用报警测试用例'''
        wait1 = WebDriverWait(self.dr, 20, 0.2)
        # 输入IMEI号
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入IMEI"]'))).send_keys('861097040964037')
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="请输入需要搜索的IMEI号"]').send_keys('097040344214')
        # time.sleep(1)
        time.sleep(5)
        # 点击查询
        # wait1.until(EC.visibility_of_element_located((
        #     By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]'))).click()
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        # time.sleep(5)
        # 点击停用报警
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
            'div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
        #     'div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]').click()
        # time.sleep(2)
        # 点击确认按钮
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//div[@class="ivu-modal-wrap vertical-center-modal'
                      ' delModal"]/div/div/div[3]/div/button[2]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//div[@class="ivu-modal-wrap vertical-center-modal delModal"]/div/div/div[3]/div/button[2]').click()
        # time.sleep(2)
        # 获取查询结果，保存在变量里
        span = wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]/span'))).text
        # span = self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
        #     'div/div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '停用报警', '停用报警失败')
        # time.sleep(2)
        # 点击清除按钮
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//div[@class="ivu-modal-wrap vertical-center-modal'
                      ' delModal"]/div/div/div[3]/div/button[2]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        # time.sleep(5)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Qybj')
    def test_ZHHL_BJFX_Qybj(self):
        '''报警分析模块-启用报警测试用例'''
        wait2 = WebDriverWait(self.dr, 20, 0.2)
        wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@placeholder="请输入IMEI"]'))).send_keys('861097040964037')
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="请输入需要搜索的IMEI号"]').send_keys('097040344214')
        # time.sleep(1)
        # 点击查询
        wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]'))).click()
        # self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        # time.sleep(5)
        # 点击启用报警
        wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
                      'div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[7]/div[1]/div[3]/div[1]'
        #     '/div[3]/table/tbody/tr/td[8]/div/button[3]').click()
        # time.sleep(2)
        # 获取查询结果，保存在变量里
        span = wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
                      'div/div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]/span'))).text
        # span = self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
        #     'div/div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[2]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '启用报警', '启用报警失败')
        # time.sleep(2)
        # 点击清除按钮
        wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//div[@class="ivu-modal-wrap vertical-center-modal'
                      ' delModal"]/div/div/div[3]/div/button[2]'))).click()

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_BJFX_TyQybj('test_ZHHL_BJFX_Tybj'))
    testunit.addTest(MyTestCase_ZHHL_BJFX_TyQybj('test_ZHHL_BJFX_Qybj'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-报警分析模块-停用启用报警测试报告',
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