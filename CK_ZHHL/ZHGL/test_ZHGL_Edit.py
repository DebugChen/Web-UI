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


class MyTestCase_ZHHL_ZHGL_Edit(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-账户管理模块-编辑测试集'''

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
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Edit1')
    def test_ZHHL_ZHGL_Edit1(self):
        '''账户管理模块-编辑测试用例-权限：读写'''
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
        # 点击编辑按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr/td[7]/div/div/button[2]').click()
        time.sleep(2)
        # 修改关联组织
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').send_keys('产品研发')
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//i[@class="ivu-icon ivu-icon-ios-search"]').click()
        time.sleep(0.5)
        # 选中组织：产品研发
        self.dr.find_element_by_xpath(
            '//*[@id="ztree2_17_check"]').click()
        time.sleep(0.5)
        # 修改联系人
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[1]/div/div/input').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[1]/div/div/input').send_keys('张三三')
        time.sleep(1)
        # 修改手机号
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[2]/div/div/input').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[2]/div/div/input').send_keys('13366666666')
        time.sleep(1)
        # 修改关联权限
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[3]/div/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中：超级管理员
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[3]/div/div/div[2]/ul[2]/li[6]').click()
        time.sleep(1)
        # 修改账号类型
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[4]/div/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中：组织
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[4]/div/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 修改数据权限：只读
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-radio-group ivu-radio-group-default ivu-radio-default"]/label[2]').click()
        time.sleep(1)
        # 修改报警类型
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/div[1]').click()
        time.sleep(1)
        # 选中：拆卸报警、移动异常
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]').click()
        time.sleep(1)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(2)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)
        # #验证是否新增成功
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="header-left"]/ul/li[1]/div/input[@type="text"]').send_keys('ceshi01')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        # 获取查询结果，保存在变量里
        div1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div'
            '/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '张三三', '编辑账号失败')
        time.sleep(1)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_ZHGL_Edit2')
    def test_ZHHL_ZHGL_Edit2(self):
        '''账户管理模块-编辑测试用例-权限：只读'''
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="header-left"]/ul/li[1]/div/input[@type="text"]').send_keys('ceshi01')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        # 点击编辑按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr/td[7]/div/div/button[2]').click()
        time.sleep(2)
        # 修改关联组织
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请搜索关联组织"]').send_keys('产品研发')
        # 点击查询按钮
        self.dr.find_element_by_xpath(
            '//i[@class="ivu-icon ivu-icon-ios-search"]').click()
        time.sleep(0.5)
        # 选中组织：产品研发
        self.dr.find_element_by_xpath(
            '//*[@id="ztree2_17_check"]').click()
        time.sleep(0.5)
        # 修改联系人
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[1]/div/div/input').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[1]/div/div/input').send_keys('张三')
        time.sleep(1)
        # 修改手机号
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[2]/div/div/input').clear()
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[2]/div/div/input').send_keys('13388888888')
        time.sleep(1)
        # 修改关联权限
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[3]/div/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中：维护人员
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[3]/div/div/div[2]/ul[2]/li[4]').click()
        time.sleep(1)
        # 修改账号类型
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[4]/div/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中：星豆
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[4]/div/div/div[2]/ul[2]/li[1]').click()
        time.sleep(1)
        # 修改数据权限：读写
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-radio-group ivu-radio-group-default ivu-radio-default"]/label[1]').click()
        time.sleep(1)
        # 修改报警类型
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/div[1]').click()
        time.sleep(1)
        # 选中：拆卸报警、移动异常
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="form-item-right"]/div[6]/div/div/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]').click()
        time.sleep(1)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(2)
        # 点击重置
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[2]').click()
        time.sleep(2)
        # #验证是否新增成功
        # 输入登录账号
        self.dr.find_element_by_xpath(
            '//div[@class="header-left"]/ul/li[1]/div/input[@type="text"]').send_keys('ceshi01')
        time.sleep(0.5)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        # 获取查询结果，保存在变量里
        div2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div'
            '/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '张三', '编辑账号失败')
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
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Edit('test_ZHHL_ZHGL_Edit1'))
    testunit.addTest(MyTestCase_ZHHL_ZHGL_Edit('test_ZHHL_ZHGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-账户管理模块-编辑测试报告',
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