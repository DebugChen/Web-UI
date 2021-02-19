import os
from BeautifulReport import BeautifulReport
import time
import unittest
from selenium.webdriver import ActionChains
import sys
sys.path.append('../Login/')
from test_Login_GG import MyTestCase_ZHHL_Login_GG


class MyTestCase_ZHHL_Xgmm(MyTestCase_ZHHL_Login_GG):
    '''城市基础设施监测平台-修改密码模块-测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\Login\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\Login\img"), img_name))

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_Xgmm1')
    def test_ZHHL_Xgmm1(self):
        '''登录模块-修改密码测试用例-新密码'''
        # 鼠标悬停在“账户管理”链接上
        link1 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')
        ActionChains(self.dr).move_to_element(link1).perform()
        time.sleep(2)
        # 点击组织管理菜单
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[2]/div/div[2]/div/p[1]').click()
        time.sleep(4)
        # 点击修改密码
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/img[3]').click()
        time.sleep(2)
        # 输入原密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入原密码"]').send_keys("Xd0020110")
        time.sleep(0.5)
        # 输入新密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入密码"]').send_keys("Ck19920308")
        time.sleep(0.5)
        # 输入确认密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请再次输入密码"]').send_keys("Ck19920308")
        time.sleep(0.5)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        p = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-success"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '操作成功', '修改密码失败')
        time.sleep(1)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_Xgmm2')
    def test_ZHHL_Xgmm2(self):
        '''登录模块-修改密码测试用例-旧密码'''
        # 输入账号
        self.dr.find_element_by_xpath('//input[@placeholder="请输入账号"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys("chenkai")
        time.sleep(1)
        # 输入密码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("Ck19920308")
        time.sleep(1)
        # 输入验证码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys("1111")
        time.sleep(1)
        # 点击登录
        self.dr.find_element_by_class_name('loginEvent').click()
        time.sleep(3)
        # 鼠标悬停在“账户管理”链接上
        link2 = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[1]/li')
        ActionChains(self.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击组织管理菜单
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/div/div[2]/div/div[2]/div/p[1]').click()
        time.sleep(3)
        # 点击修改密码
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/img[3]').click()
        time.sleep(2)
        # 输入原密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入原密码"]').send_keys("Ck19920308")
        time.sleep(0.5)
        # 输入新密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入密码"]').send_keys("Xd0020110")
        time.sleep(0.5)
        # 输入确认密码
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请再次输入密码"]').send_keys("Xd0020110")
        time.sleep(0.5)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//div[@class="ivu-modal-wrap vertical-center-modal none-header-footer-border"]'
            '/div/div/div[3]/div/div[2]/button').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        p = self.dr.find_element_by_xpath(
            '//div[@class="ivu-message-custom-content ivu-message-success"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '操作成功', '修改密码失败')
        time.sleep(1)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 执行测试用例
    testunit.addTest(MyTestCase_ZHHL_Xgmm('test_ZHHL_Xgmm1'))
    testunit.addTest(MyTestCase_ZHHL_Xgmm('test_ZHHL_Xgmm2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-登录模块-修改密码测试报告',
                  description='城市基础设施监测平台-登录模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp,
    #                           title='车辆监控平台UI自动化测试报告',
#                               description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)