import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase_CLJK_Xgmm(unittest.TestCase):
    '''车辆监控平台-登录模块-修改密码测试集'''

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
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\KHXXGL\image1\KHXXGL_Add.png')
        # 关闭浏览器
        cls.dr.quit()

    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Xgmm1')
    def test_CLJK_KHXXGL_Xgmm1(self):
        '''登录模块-修改密码测试用例-新密码'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 输入用户名
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('chenkai')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_id("username")).send_keys("chenkai")
        # 输入密码
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Xd0020110')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_id("password")).send_keys("Xd0020110")
        # 输入验证码
        wait.until(EC.visibility_of_element_located((By.ID, "code"))).send_keys('1234')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_id("code")).send_keys("1234")
        # 点击登录按钮
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@value="登录"]'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath('//input[@value="登录"]')).click()
        time.sleep(2)
        # 鼠标悬停在“客户资料管理”链接上
        link = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div/ul/li[2]')
        ActionChains(self.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“客户信息管理”链接上
        link2 = self.dr.find_element_by_xpath(
            '/html/body/div[2]/ul/li[1]/ul/li')
        ActionChains(self.dr).move_to_element(link2).perform()
        time.sleep(1)
        # 点击客户信息管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '/html/body/div[2]/ul/li[1]/ul/li'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '/html/body/div[2]/ul/li[1]/ul/li')).click()
        time.sleep(2)
        # 点击修改密码按钮
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[4]/p[1]/button'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath('//*[@id="app"]/div/div[4]/p[1]/button')).click()
        # 输入原密码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//form[@class="el-form demo-ruleForm"]/div[1]/div/div[1]/input'))).\
            send_keys('Xd0020110')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//form[@class="el-form demo-ruleForm"]/div[1]/div/div[1]/input'))\
        #     .send_keys('Xd0020110')
        # 输入新密码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//form[@class="el-form demo-ruleForm"]/div[2]/div/div/input'))).\
            send_keys('Ck19920308')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//form[@class="el-form demo-ruleForm"]/div[2]/div/div/input'))\
        #     .send_keys('Ck19920308')
        # 确认新密码
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//form[@class="el-form demo-ruleForm"]/div[3]/div/div/input'))).\
            send_keys('Ck19920308')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//form[@class="el-form demo-ruleForm"]/div[3]/div/div/input'))\
        #     .send_keys('Ck19920308')
        # 点击提交按钮
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[5]/div/div[3]/span/button[1]'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[5]/div/div[3]/span/button[1]')).click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[4]/label/span[2]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '记住密码', '修改密码失败')

    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Xgmm2')
    def test_CLJK_KHXXGL_Xgmm2(self):
        '''登录模块-修改密码测试用例-旧密码'''
        wait1 = WebDriverWait(self.dr, 10, 0.2)
        # 输入用户名
        wait1.until(EC.visibility_of_element_located((
            By.ID, 'username'))).clear()
        wait1.until(EC.visibility_of_element_located((
            By.ID, 'username'))).send_keys("chenkai")
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_id("username")).clear()
        # self.dr.find_element_by_id("username").send_keys("chenkai")
        # 输入密码
        wait1.until(EC.visibility_of_element_located((
            By.ID, 'password'))).clear()
        wait1.until(EC.visibility_of_element_located((
            By.ID, 'password'))).send_keys("Ck19920308")
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_id("password")).clear()
        # self.dr.find_element_by_id("password").send_keys("Ck19920308")
        # 输入验证码
        wait1.until(EC.visibility_of_element_located((
            By.ID, 'code'))).send_keys("1234")
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_id("code")).send_keys("1234")
        # 点击登录按钮
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//input[@value="登录"]'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath('//input[@value="登录"]')).click()
        time.sleep(2)
        # 鼠标悬停在“客户资料管理”链接上
        link = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div/ul/li[2]')
        ActionChains(self.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“客户信息管理”链接上
        link2 = self.dr.find_element_by_xpath(
            '/html/body/div[2]/ul/li[1]/ul/li')
        ActionChains(self.dr).move_to_element(link2).perform()
        time.sleep(1)
        # 点击客户信息管理菜单
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '/html/body/div[2]/ul/li[1]/ul/li'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '/html/body/div[2]/ul/li[1]/ul/li')).click()
        time.sleep(2)
        # 点击修改密码按钮
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[4]/p[1]/button'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath('//*[@id="app"]/div/div[4]/p[1]/button')).click()
        # 输入原密码
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//form[@class="el-form demo-ruleForm"]/div[1]/div/div[1]/input')))\
            .send_keys('Ck19920308')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//form[@class="el-form demo-ruleForm"]/div[1]/div/div[1]/input'))\
        #     .send_keys('Ck19920308')
        # 输入新密码
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//form[@class="el-form demo-ruleForm"]/div[2]/div/div/input'))) \
            .send_keys('Xd0020110')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//form[@class="el-form demo-ruleForm"]/div[2]/div/div/input'))\
        #     .send_keys('Xd0020110')
        # 确认新密码
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//form[@class="el-form demo-ruleForm"]/div[3]/div/div/input'))) \
            .send_keys('Xd0020110')
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//form[@class="el-form demo-ruleForm"]/div[3]/div/div/input'))\
        #     .send_keys('Xd0020110')
        # 点击提交按钮
        wait1.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[5]/div/div[3]/span/button[1]'))).click()
        # WebDriverWait(self.dr, 10).until \
        #     (lambda dr:self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[5]/div/div[3]/span/button[1]')).click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div[4]/label/span[2]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '记住密码', '修改密码失败')

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 定义测试报告
    testunit.addTest(MyTestCase_CLJK_Xgmm('test_CLJK_KHXXGL_Xgmm1'))
    testunit.addTest(MyTestCase_CLJK_Xgmm('test_CLJK_KHXXGL_Xgmm2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-登录模块-修改密码测试报告',
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