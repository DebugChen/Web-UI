import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_CLJK_KHXXGL_Logout(unittest.TestCase):
    '''车辆监控平台-客户信息管理模块-注销测试集'''

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
            '//div[@class="happy-scroll-content"]/div/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“客户信息管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[HT_XBDY]/ul/li')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击客户信息管理菜单
        cls.dr.find_element_by_xpath("/html/body/div[2]/ul/li[HT_XBDY]/ul/li").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\LSTZ\image1\KHXXGL_Logout.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Logout')
    def test_CLJK_KHXXGL_Logout(self):
        '''客户信息管理模块-注销测试用例'''
        # 查询需要注销的客户信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').send_keys('诚连科技')
        # 点击搜索按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # # #取消注销
        # # 点击注销按钮
        # self.dr.find_element_by_xpath(
        #     '//table[@class="el-table__body"]/tbody/tr/td/div/button[4]').click()
        # time.sleep(2)
        # # 点击取消按钮
        # self.dr.find_element_by_xpath(
        # '//div[@class="el-message-box"]/div[3]/button[HT_XBDY]').click()
        # time.sleep(2)
        # #注销成功
        # 点击注销按钮
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td/div/button[4]').click()
        time.sleep(2)
        # 点击确认按钮
        self.dr.find_element_by_xpath(
            '//div[@class="el-message-box"]/div[3]/button[2]').click()
        time.sleep(3)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 定义变量，用于存放页面元素
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '注销', '注销客户失败')
        time.sleep(2)

if __name__=='__main__':
    # 执行测试用例
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Logout('test_CLJK_KHXXGL_Logout'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-客户信息管理模块-注销测试报告',
                  description='车辆监控平台-客户信息管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)