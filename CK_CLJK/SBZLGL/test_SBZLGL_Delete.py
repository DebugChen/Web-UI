import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_CLJK_SBZLGL_Delete(unittest.TestCase):
    '''车辆监控平台-设备资料管理模块-删除测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_CLJK\SBZLGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\SBZLGL\img"), img_name))

    @classmethod
    # 启动测试用例方法
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")
        # 输入用户名
        cls.dr.find_element_by_id("username").send_keys("chenkai")
        time.sleep(3)
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Xd0020110")
        time.sleep(3)
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
        # 鼠标悬停在“设备资料管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul/li')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击设备资料管理
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul/li').click()
        time.sleep(7)

    @classmethod
    # 关闭测试用例方法
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\SBZLGL\image\SBZLGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBZLGL_Delete')
    def test_CLJK_SBZLGL_Delete(self):
        '''设备资料管理模块-删除测试用例'''
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索IMEI号"]').send_keys('861097040098216')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(4)
        # 点击删除按钮
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[7]/div/button[3]').click()
        time.sleep(1)
        # 点击确认按钮
        self.dr.find_element_by_xpath('//div[@aria-label="提示"]/div/div[3]/button[2]').click()
        time.sleep(3)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(4)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div[2]/div/div/span[1]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '共 0 条', '删除设备失败')
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_SBZLGL_Delete('test_CLJK_SBZLGL_Delete'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-设备资料管理模块-删除测试报告',
                  description='车辆监控平台-设备资料管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)