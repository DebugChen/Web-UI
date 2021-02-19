import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_APPZHGL_Edit(unittest.TestCase):
    '''车辆监控平台-APP账户管理模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\APPZHGL\img"), img_name))

    @classmethod
    # 启动测试用例方法
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")
        # 输入用户名
        cls.dr.find_element_by_id("username").send_keys("chenkai")
        time.sleep(1)
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Ck19920308")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“后台系统管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[5]')
        ActionChains(cls.dr).move_to_element(link).perform()
        # self.dr.implicitly_wait(5)
        time.sleep(1)
        # 鼠标悬停在“APP账户管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击APP账户管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul').click()
        time.sleep(2)

    # 关闭测试用例方法
    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\FWQDKGL\image\APPZHGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_APPZHGL_Edit1')
    def test_CLJK_APPZHGL_Edit1(self):
        '''APP账户管理模块-编辑测试用例-发送安装信息'''
        # 输入IMEI信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI"]').send_keys('867282034954482')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[5]/div/button').click()
        time.sleep(2)
        # 修改手机号
        self.dr.find_element_by_xpath('//form[@class="el-form"]/div[2]/div/div/input').clear()
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[2]/div/div/input').send_keys('13444444442')
        time.sleep(1)
        # 选择是否发送安装信息（发送）
        self.dr.find_element_by_xpath('//form[@class="el-form"]/div[3]/div/div/div/input').click()
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[3]/div/div/div/input').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[3]/div/div/div/input').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div/div[3]/div/button[HT_XBDY]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '13444444442', '编辑APP账户失败')
        time.sleep(1)
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '发送安装信息', '编辑APP账户失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除所有条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_APPZHGL_Edit2')
    def test_CLJK_APPZHGL_Edit2(self):
        '''APP账户管理模块-编辑测试用例-不发送安装信息'''
        # 输入IMEI信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI"]').send_keys('867282034954482')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[5]/div/button').click()
        time.sleep(2)
        # 修改手机号
        self.dr.find_element_by_xpath('//form[@class="el-form"]/div[2]/div/div/input').clear()
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[2]/div/div/input').send_keys('13444444666')
        time.sleep(1)
        # 选择是否发送安装信息（不发送）
        self.dr.find_element_by_xpath('//form[@class="el-form"]/div[3]/div/div/div/input').click()
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[3]/div/div/div/input').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[3]/div/div/div/input').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div/div[3]/div/button[HT_XBDY]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '13444444666', '编辑APP账户失败')
        time.sleep(1)
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '不发送安装信息', '编辑APP账户失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除所有条件"]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_APPZHGL_Edit('test_CLJK_APPZHGL_Edit1'))
    testunit.addTest(MyTestCase_CLJK_APPZHGL_Edit('test_CLJK_APPZHGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-APP账户管理模块-编辑测试报告',
                  description='车辆监控平台-APP账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)