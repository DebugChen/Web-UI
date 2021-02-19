import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_CLJK_JSQXGL_Edit(unittest.TestCase):
    '''车辆监控平台-角色权限管理模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\JSQXGL\img"), img_name))

    @classmethod
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
        cls.dr.find_element_by_id("password").send_keys("Xd0020110")
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
        # 鼠标悬停在“角色权限管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[1]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击角色权限管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[1]/ul').click()
        time.sleep(2)

    # 关闭测试用例方法
    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\SBJK\image\JSQXGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_JSQXGL_Edit1')
    def test_CLJK_JSQXGL_Edit1(self):
        '''角色权限管理模块-编辑测试用例-角色状态：锁定'''
        # 输入角色名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的角色名称"]').send_keys('测试角色02')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div/button[2]').click()
        time.sleep(2)
        # 修改角色名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入角色名称，不可包含数字和特殊字符"]').clear()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入角色名称，不可包含数字和特殊字符"]').send_keys('测试角色022')
        time.sleep(1)
        # 选择角色状态：锁定
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[2]/div/label[2]/span[1]/span').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div/div[3]/div/button[1]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '测试角色022', '编辑角色失败')
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '锁定', '编辑角色失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_JSQXGL_Edit2')
    def test_CLJK_JSQXGL_Edit2(self):
        '''角色权限管理模块-编辑测试用例-角色状态：正常'''
        # 输入角色名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的角色名称"]').send_keys('测试角色022')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div/button[2]').click()
        time.sleep(2)
        # 输入角色名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入角色名称，不可包含数字和特殊字符"]').clear()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入角色名称，不可包含数字和特殊字符"]').send_keys('测试角色02')
        time.sleep(1)
        # 选择角色状态：正常
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[2]/div/label[1]/span[1]/span').click()
        time.sleep(1)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div/div[3]/div/button[1]').click()
        time.sleep(2)
        # 清除角色名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的角色名称"]').clear()
        # 输入角色名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的角色名称"]').send_keys('测试角色02')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '测试角色02', '编辑角色失败')
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '正常', '编辑角色失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_JSQXGL_Edit('test_CLJK_JSQXGL_Edit1'))
    testunit.addTest(MyTestCase_CLJK_JSQXGL_Edit('test_CLJK_JSQXGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-角色权限管理模块-编辑测试报告',
                  description='车辆监控平台-角色权限管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)