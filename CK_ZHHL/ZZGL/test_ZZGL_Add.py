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


class MyTestCase_ZHHL_ZZGL_Add(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-组织管理模块-新增测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\ZZGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\ZZGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_ZZGL_Add1')
    def test_ZHHL_ZZGL_Add1(self):
        '''组织管理模块-新增测试用例'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 鼠标悬停在“系统管理”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')))
        ActionChains(self.dr).move_to_element(link).perform()
        # 点击组织管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//p[.="组织管理"]'))).click()
        time.sleep(3)
        # 点击新增组织按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/button').click()
        time.sleep(1)
        # 输入组织名称
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[1]/div/div/input').send_keys('测试组织02')
        time.sleep(0.5)
        # 输入联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('张三')
        time.sleep(0.5)
        # 输入联系电话
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系电话"]').send_keys('13367889870')
        time.sleep(0.5)
        # 输入地址
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入地址"]').send_keys('武汉市')
        time.sleep(0.5)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(4)
        # #验证组织是否添加成功
        # 输入组织名称
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/div/input')\
            .send_keys('测试组织02')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '测试组织02', '新增组织失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(3)

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_ZZGL_Add2')
    def test_ZHHL_ZZGL_Add2(self):
        '''组织管理模块-新增测试用例'''
        # 点击新增组织按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/button').click()
        time.sleep(1)
        # 输入组织名称
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[2]/div/form/div[1]/div/div/input').send_keys('测试组织02')
        time.sleep(0.5)
        # 输入联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('测试组织02')
        time.sleep(0.5)
        # 输入联系电话
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系电话"]').send_keys('13367889877')
        time.sleep(0.5)
        # 输入地址
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入地址"]').send_keys('武汉市')
        time.sleep(0.5)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(2)
        # #验证组织是否添加成功
        # 输入组织名称
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/ul/li[1]/div/input')\
            .send_keys('测试组织02')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[1]/div/div/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, '测试组织02', '新增组织失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(3)

if __name__=='__main__':
    # 执行测试用例
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_ZZGL_Add('test_ZHHL_ZZGL_Add1'))
    testunit.addTest(MyTestCase_ZHHL_ZZGL_Add('test_ZHHL_ZZGL_Add2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-组织管理模块-新增测试报告',
                  description='城市基础设施监测平台-组织管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)