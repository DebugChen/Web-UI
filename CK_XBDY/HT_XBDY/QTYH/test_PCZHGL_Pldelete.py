import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_CLJK_PCZHGL_Pldelete(unittest.TestCase):
    '''车辆监控平台-PC账户管理模块-批量删除测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\PCZHGL\img"), img_name))

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
            '//*[@id="app"]/div/div[HT_XBDY]/div/div[HT_XBDY]/div/div/ul/li[5]')
        ActionChains(cls.dr).move_to_element(link).perform()
        # self.dr.implicitly_wait(5)
        time.sleep(1)
        # 鼠标悬停在“PC账户管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击PC账户管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\QTYH\image\PCZHGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_PCZHGL_Pldelete')
    def test_CLJK_PCZHGL_Pldelete(self):
        '''PC账户管理模块-批量删除测试用例'''
        # 输入用户账户
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的用户账号"]').send_keys('lwl')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 选择需要删除账户
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[4]/td[HT_XBDY]/div/label/span/span').click()
        time.sleep(2)
        # 点击批量删除
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[HT_XBDY]/div[2]/button[2]').click()
        time.sleep(2)
        # 点击确认
        self.dr.find_element_by_xpath(
            '//div[@aria-label="提示"]/div/div[3]/button[2]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[HT_XBDY]/div[3]/div[2]/div/div/span[HT_XBDY]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '共 6 条', '批量删除PC账户失败')
        time.sleep(1)
        # # 点击清除
        # self.dr.find_element_by_xpath('//button[@title="清除所有条件"]').click()
        # time.sleep(2)
        # 关闭PC账户管理界面
        self.dr.find_element_by_xpath('//*[@id="tab-/userManage"]/span[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_PCZHGL_Pldelete('test_CLJK_PCZHGL_Pldelete'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-PC账户管理模块-批量删除测试报告',
                  description='车辆监控平台-PC账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)