import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_AZTJFX_Ckraz(unittest.TestCase):
    '''车辆监控平台-安装统计分析模块-查看日安装测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\AZTJFX\img"), img_name))

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
        # 鼠标悬停在“数据统计分析”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[4]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击安装统计分析菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul').click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\AZTJFX\image\AZTJFX_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_AZTJFX_Ckraz')
    def test_CLJK_AZTJFX_Ckraz(self):
        '''安装统计分析模块-查看日安装测试用例'''
        # 选择时间
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的月份"]').click()
        time.sleep(2)
        # 选中九月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[3]/td[1]/div').click()
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 点击查看日安装
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[7]/div/button').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[1]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '日安装分析（台）', '查看日安装失败')
        time.sleep(2)
        # 点击关闭窗口
        self.dr.find_element_by_xpath('//div[@aria-label="日安装分析（台）"]/div/button').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_AZTJFX_Ckraz('test_CLJK_AZTJFX_Ckraz'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-安装统计分析模块-查看日安装测试报告',
                  description='车辆监控平台-安装统计分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)