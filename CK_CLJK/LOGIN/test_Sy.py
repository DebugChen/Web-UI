import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase_CLJK_Sy(unittest.TestCase):
    '''车辆监控平台-首页模块-快捷导航测试集'''

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
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")
        wait = WebDriverWait(cls.dr, 10, 0.2)
        # 输入用户名
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("chenkai")
        # 输入密码
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("Xd0020110")
        # 输入验证码
        wait.until(EC.visibility_of_element_located((By.ID, "code"))).send_keys("1234")
        # 点击登录按钮
        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@value="登录"]'))).click()
        # time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\KHXXGL\image1\KHXXGL_Add.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SY_Bjtjfx')
    def test_CLJK_SY_Bjtjfx(self):
        '''首页模块-报警统计分析快捷导航测试用例'''
        wait1 = WebDriverWait(self.dr, 10, 0.2)
        # 点击报警统计分析导航菜单
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[1]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[1]').click()
        # time.sleep(9)
        # 获取页面元素，保存到变量
        span = wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div/button/span'))).text
        # span = self.dr.find_element_by_xpath(
        #     '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div/button/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '历史报警', '报警统计分析导航失败')
        time.sleep(1)
        # 关闭报警统计分析界面
        self.dr.find_element_by_xpath(
            '//*[@id="tab-/alarmAnalysis"]/span[2]').click()
        # time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SY_Aztjfx')
    def test_CLJK_SY_Aztjfx(self):
        '''首页模块-安装统计分析快捷导航测试用例'''
        wait2 = WebDriverWait(self.dr, 10, 0.2)
        # 点击安装统计分析导航菜单
        wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[2]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[2]').click()
        # time.sleep(5)
        # 获取页面元素，保存到变量
        div = wait2.until(EC.visibility_of_element_located((
            By.XPATH, '//table[@class="el-table__header"]/thead/tr/th[4]/div'))).text
        # div = self.dr.find_element_by_xpath(
        #     '//table[@class="el-table__header"]/thead/tr/th[4]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '安装数量（台）', '安装统计分析导航失败')
        time.sleep(1)
        # 关闭安装统计分析界面
        # wait2.until(EC.visibility_of_element_located((
        #     By.XPATH, '//*[@id="tab-/mtAnalysis"]/span[2]'))).click()
        self.dr.find_element_by_xpath(
            '//*[@id="tab-/mtAnalysis"]/span[2]').click()
        # time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SY_Lctjfx')
    def test_CLJK_SY_Lctjfx(self):
        '''首页模块-里程统计分析快捷导航测试用例'''
        wait3 = WebDriverWait(self.dr, 15, 0.2)
        # 点击里程统计分析导航菜单
        wait3.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[3]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[3]').click()
        # time.sleep(12)
        # 获取页面元素，保存到变量
        div = wait3.until(EC.visibility_of_element_located((
            By.XPATH, '//table[@class="el-table__header"]/thead/tr/th[4]/div'))).text
        # div = self.dr.find_element_by_xpath(
        #     '//table[@class="el-table__header"]/thead/tr/th[4]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '月里程 (公里)', '里程统计分析导航失败')
        time.sleep(1)
        # 关闭里程统计分析界面
        # wait3.until(EC.visibility_of_element_located((
        #     By.XPATH, '//*[@id="tab-/mileageManager"]/span[2]'))).click()
        self.dr.find_element_by_xpath(
            '//*[@id="tab-/mileageManager"]/span[2]').click()
        # time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SY_Dqtjfx')
    def test_CLJK_SY_Dqtjfx(self):
        '''首页模块-盗抢统计分析快捷导航测试用例'''
        wait4 = WebDriverWait(self.dr, 20, 0.2)
        # 点击盗抢统计分析导航菜单
        wait4.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[4]'))).click()
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[6]/div[4]/div/div[5]/div[2]/ul/li[4]').click()
        # time.sleep(8)
        # 获取页面元素，保存到变量
        span = wait4.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="mymap"]/button/span'))).text
        # span = self.dr.find_element_by_xpath(
        #     '//*[@id="mymap"]/button/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '清除所有点', '盗抢统计分析导航失败')
        time.sleep(8)
        # 关闭盗抢统计分析界面
        # wait4.until(EC.visibility_of_element_located((
        #     By.XPATH, '//*[@id="tab-/stolen"]/span[2]'))).click()
        self.dr.find_element_by_xpath(
            '//*[@id="tab-/stolen"]/span[2]').click()
        # time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_Sy('test_CLJK_SY_Bjtjfx'))
    testunit.addTest(MyTestCase_CLJK_Sy('test_CLJK_SY_Aztjfx'))
    testunit.addTest(MyTestCase_CLJK_Sy('test_CLJK_SY_Lctjfx'))
    testunit.addTest(MyTestCase_CLJK_Sy('test_CLJK_SY_Dqtjfx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-首页模块-快捷导航测试报告',
                  description='车辆监控平台-首页模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 定义测试报告存放路径
    # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)