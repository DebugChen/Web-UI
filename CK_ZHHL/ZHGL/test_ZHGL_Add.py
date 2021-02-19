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


class MyTestCase_ZHHL_ZHGL_Add(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-账号管理模块-新增测试集'''

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
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Add1')
    def test_ZHHL_ZHGL_Add1(self):
        '''账号管理模块-新增测试用例'''
        wait = WebDriverWait(self.dr, 10, 0.2)
        # 鼠标悬停在“系统管理”链接上
        link = wait.until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')))
        ActionChains(self.dr).move_to_element(link).perform()
        # 点击账号管理菜单
        wait.until(EC.visibility_of_element_located((
            By.XPATH, '//p[.="账号管理"]'))).click()
        time.sleep(3)
        # 点击新增账号
        self.dr.find_element_by_xpath(
            '//div[@class="btnGroud"]/button[@type="button"]').click()
        time.sleep(0.5)
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-left"]'
            '/div[@class="ivu-form-item ivu-form-item-required"]/div'
            '[@class="ivu-form-item-content"]/div/input[@type="text"]').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-left"]'
            '/div[@class="ivu-form-item ivu-form-item-required"]/div'
            '[@class="ivu-form-item-content"]/div/input[@type="text"]').send_keys('ceshi02')
        time.sleep(0.5)
        # 输入关联组织
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').send_keys('软件部')
        time.sleep(0.5)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//i[@class="ivu-icon ivu-icon-ios-search"]').click()
        time.sleep(1)
        # 选中组织：软件部
        self.dr.find_element_by_xpath(
            '//ul[@class="level1 line"]/li[3]/span[2]').click()
        time.sleep(0.5)
        # 输入登录密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入登录密码"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入登录密码"]')\
            .send_keys('Douniu2918')
        time.sleep(0.5)
        # 输入联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('李四')
        time.sleep(0.5)
        # 输入手机号
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-right"]'
            '/div[3]/div[@class="ivu-form-item-content"]/div/input[@type="text"]')\
            .send_keys('13333333333')
        time.sleep(1)
        # 选择关联权限
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[4]/div[@class="ivu-form-item-content"]'
            '/div//span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中：维护人员
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[4]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[4]').click()
        time.sleep(1)
        # 选择账号类型
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[5]/div[@class="ivu-form-item-content"]'
            '/div//span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中：星豆
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[5]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[1]').click()
        time.sleep(1)
        # 选择数据权限：读写
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/label[1]').click()
        time.sleep(1)
        # 选择报警类型
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-right"]'
            '/div[7]/div[@class="ivu-form-item-content"]/div/div[1]/div/'
            'span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中：倾斜告警、拆卸报警
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[7]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[1]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[7]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[2]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]').click()
        time.sleep(1)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(3)
        # 防止新增失败，关闭窗口
        try:
            A1 = self.dr.find_element_by_xpath(
                '//div[@class="ivu-modal-wrap vertical-center-modal '
                'none-header-footer-border"]/div/div/div[1]/div/img')
        except:
            print("新增成功")
        else:
            print("新增失败")
            self.save_img('001')
            A1.click()
        # #验证是否新增成功
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="header-left"]/ul/li[1]/div/input[@type="text"]').send_keys('ceshi02')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span1, 'ceshi02', '新增账号失败')
        # 获取查询结果，保存在变量里
        span2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span2, '李四', '新增账号失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Add2')
    def test_ZHHL_ZHGL_Add2(self):
        '''账号管理模块-新增测试用例'''
        # 点击新增账号
        self.dr.find_element_by_xpath(
            '//div[@class="btnGroud"]/button[@type="button"]').click()
        time.sleep(0.5)
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-left"]'
            '/div[@class="ivu-form-item ivu-form-item-required"]/div'
            '[@class="ivu-form-item-content"]/div/input[@type="text"]').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-left"]'
            '/div[@class="ivu-form-item ivu-form-item-required"]/div'
            '[@class="ivu-form-item-content"]/div/input[@type="text"]').send_keys('ceshi02')
        time.sleep(0.5)
        # 输入关联组织
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').send_keys('软件部')
        time.sleep(0.5)
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//i[@class="ivu-icon ivu-icon-ios-search"]').click()
        time.sleep(1)
        # 选中组织：软件部
        self.dr.find_element_by_xpath(
            '//ul[@class="level1 line"]/li[3]/span[2]').click()
        time.sleep(0.5)
        # 输入登录密码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入登录密码"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入登录密码"]').send_keys('Douniu2918')
        time.sleep(0.5)
        # 输入联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('王五')
        time.sleep(0.5)
        # 输入手机号
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-right"]'
            '/div[3]/div[@class="ivu-form-item-content"]/div/input[@type="text"]').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-right"]'
            '/div[3]/div[@class="ivu-form-item-content"]/div/input[@type="text"]') \
            .send_keys('13555555555')
        time.sleep(1)
        # 选择关联权限
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[4]/div[@class="ivu-form-item-content"]'
            '/div//span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中：维护人员
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[4]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[5]').click()
        time.sleep(1)
        # 选择账号类型
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[5]/div[@class="ivu-form-item-content"]'
            '/div//span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中：星豆
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[5]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[2]').click()
        time.sleep(1)
        # 选择数据权限：只读
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/label[2]').click()
        time.sleep(1)
        # 选择报警类型
        self.dr.find_element_by_xpath(
            '//div[@class="contain user-info-opt"]/form/div[@class="form-item-right"]'
            '/div[7]/div[@class="ivu-form-item-content"]/div/div[1]/div/'
            'span[@class="ivu-select-placeholder"]').click()
        time.sleep(1)
        # 选中：倾斜告警、拆卸报警、移动异常
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[7]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[1]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[7]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[2]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//form/div[@class="form-item-right"]/div[7]/div[@class="ivu-form-item-content"]/div'
            '/div[@class="ivu-select-dropdown"]/ul[@class="ivu-select-dropdown-list"]/li[3]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]').click()
        time.sleep(1)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        # 防止新增失败，关闭窗口
        try:
            A2 = self.dr.find_element_by_xpath(
                '//div[@class="ivu-modal-wrap vertical-center-modal '
                'none-header-footer-border"]/div/div/div[1]/div/img')
        except:
            print("新增成功")
        else:
            self.save_img('002')
            print("新增失败")
            A2.click()
        # #验证是否新增成功
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="header-left"]/ul/li[1]/div/input[@type="text"]').send_keys('ceshi02')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        span3 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span3, 'ceshi02', '新增账号失败')
        # 获取查询结果，保存在变量里
        span4 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div[1]'
            '/div[2]/table/tbody/tr/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span4, '王五', '新增账号失败')
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
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Add('test_ZHHL_ZHGL_Add1'))
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Add('test_ZHHL_ZHGL_Add2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-账号管理模块-新增测试报告',
                  description='城市基础设施监测平台-账号管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)