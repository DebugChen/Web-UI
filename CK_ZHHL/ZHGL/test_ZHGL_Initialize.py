import os
from BeautifulReport import BeautifulReport
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_ZHGL_Initialize(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-账户管理模块-重置密码测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\ZHGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\ZHGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Initialize')
    def test_ZHHL_ZHGL_Initialize(self):
        '''账户管理模块-重置密码测试用例'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 鼠标悬停在“系统管理”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')))
        ActionChains(self.dr).move_to_element(link).perform()
        # 点击账号管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//p[.="账号管理"]'))).click()
        time.sleep(2)
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="header-left"]/ul/li[1]/div/input[@type="text"]').send_keys('ceshi01')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        # 点击重置密码
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div'
            '/div[1]/div[2]/table/tbody/tr/td[7]/div/div/button[1]').click()
        time.sleep(1)
        # 点击确认
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal delModal"]'
            '/div/div/div[3]/div/button[2]').click()
        time.sleep(1)
        # 获取查询结果，保存在变量里
        span1 = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-success"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '操作成功', '重置账号密码失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Initialize('test_ZHHL_ZHGL_Initialize'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-账户管理模块-重置密码测试报告',
                  description='城市基础设施监测平台-账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)