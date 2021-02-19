from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
import os
from BeautifulReport import BeautifulReport


class MyTestCase_CLJK_KHXXGL_Khqy(unittest.TestCase):
    '''车辆监控平台-客户信息管理模块-客户迁移测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\KHXXGL\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")
        time.sleep(2)
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
        time.sleep(2)
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[HT_XBDY]/div/div[HT_XBDY]/div/div/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“客户信息管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[HT_XBDY]/ul/li')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击客户信息菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[HT_XBDY]/ul/li').click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\LSTZ\image1\KHXXGL_Khqy.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Khqy')
    def test_CLJK_KHXXGL_Khqy(self):
        '''客户信息管理模块-客户迁移测试用例'''
        # 点击客户迁移按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[HT_XBDY]/div[2]/button[2]').click()
        time.sleep(2)
        # 搜索需要迁移客户
        self.dr.find_element_by_xpath(
            '//input[@id="searchData2"]').send_keys('天门')
        time.sleep(1)
        # 点击搜索按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[6]/div/div[2]/div/div[HT_XBDY]/div[HT_XBDY]/i').click()
        time.sleep(1)
        # 选中天门
        self.dr.find_element_by_link_text('南建-天门').click()
        time.sleep(1)
        # 选中黄冈
        self.dr.find_element_by_link_text('南建-黄冈').click()
        time.sleep(1)
        # 点击展开右侧车辆监控中心
        self.dr.find_element_by_id('ztree3_1_switch').click()
        time.sleep(2)
        # 选中目标客户（公司员工账户）
        self.dr.find_element_by_xpath('//a[@id="ztree3_4_a"][@title="公司员工账户"]').click()
        time.sleep(2)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[6]/div/div[3]/div/button[HT_XBDY]').click()
        time.sleep(4)
        # 点击关闭按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[6]/div/div[3]/div/button[2]').click()
        time.sleep(2)
        # 点击客户迁移按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[HT_XBDY]/div[2]/button[2]').click()
        time.sleep(2)
        # 点击展开左侧车辆监控中心
        self.dr.find_element_by_id('ztree2_1_switch').click()
        time.sleep(1)
        # 点击展开公司员工账户
        self.dr.find_element_by_id('ztree2_4_switch').click()
        time.sleep(1)
        # 定义变量，存在参数
        span = self.dr.find_element_by_id('ztree2_11_span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '南建-黄冈', '客户迁移失败')
        time.sleep(1)
        # 定义变量，存在参数
        span = self.dr.find_element_by_id('ztree2_12_span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '南建-天门', '客户迁移失败')
        time.sleep(2)
        # 点击关闭按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[6]/div/div[3]/div/button[2]').click()
        time.sleep(3)

if __name__=='__main__':
    # 执行测试用例
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Khqy('test_CLJK_KHXXGL_Khqy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-客户信息管理模块-客户迁移测试报告',
                  description='车辆监控平台-客户信息管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)