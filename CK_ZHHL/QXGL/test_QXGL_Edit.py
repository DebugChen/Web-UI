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


class MyTestCase_ZHHL_QXGL_Edit(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-权限管理模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\QXGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\QXGL\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_QXGL_Edit1')
    def test_ZHHL_QXGL_Edit1(self):
        '''权限管理模块-编辑测试用例-权限：组织'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 鼠标悬停在“系统管理”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')))
        ActionChains(self.dr).move_to_element(link).perform()
        # 点击权限管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//p[.="权限管理"]'))).click()
        time.sleep(2)
        # 输入权限名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').send_keys('测试权限04')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 点击编辑按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div'
            '/div[1]/div[2]/table/tbody/tr/td[6]/div/div/button[1]').click()
        time.sleep(2)
        # 修改权限名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').send_keys('测试权限044')
        time.sleep(0.5)
        # 修改权限描述
        self.dr.find_element_by_xpath(
            '//textarea[@placeholder="请输入权限描述"]').clear()
        self.dr.find_element_by_xpath(
            '//textarea[@placeholder="请输入权限描述"]').send_keys('测试权限044')
        time.sleep(1)
        # 修改权限：组织
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[2]/div[3]/div/div/form/div[3]/div/div[1]/div/label[1]').click()
        # time.sleep(0.3)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/form/div[3]/div/div[1]/div/label[2]').click()
        time.sleep(1)
        # 选中权限：系统管理、首页、工作中心
        self.dr.find_element_by_xpath(
            '//*[@id="ztreeMune_1_check"]').click()
        time.sleep(0.5)
        self.dr.find_element_by_xpath(
            '//*[@id="ztreeMune_5_check"]').click()
        time.sleep(0.5)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/form/div[4]/div/div/div[2]/button').click()
        time.sleep(3)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)
        # 输入权限名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').send_keys('测试权限044')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
            'div[1]/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '测试权限044', '编辑权限失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_QXGL_Edit2')
    def test_ZHHL_QXGL_Edit2(self):
        '''权限管理模块-编辑测试用例-权限：星豆'''
        # 输入权限名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').send_keys('测试权限044')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 点击编辑按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div'
            '/div[1]/div[2]/table/tbody/tr/td[6]/div/div/button[1]').click()
        time.sleep(2)
        # 修改权限名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').send_keys('测试权限04')
        time.sleep(0.5)
        # 修改权限描述
        self.dr.find_element_by_xpath(
            '//textarea[@placeholder="请输入权限描述"]').clear()
        self.dr.find_element_by_xpath(
            '//textarea[@placeholder="请输入权限描述"]').send_keys('测试权限04')
        time.sleep(1)
        # 修改权限：星豆
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/form/div[3]/div/div[1]/div/label[1]').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/form/div[4]/div/div/div[2]/button').click()
        time.sleep(3)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)
        # 输入权限名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入权限名称"]').send_keys('测试权限04')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
            'div[1]/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, '测试权限04', '编辑权限失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_QXGL_Edit('test_ZHHL_QXGL_Edit1'))
    testunit.addTest(MyTestCase_ZHHL_QXGL_Edit('test_ZHHL_QXGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-权限管理模块-编辑测试报告',
                  description='城市基础设施监测平台-权限管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)