import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_ZHHL_AZXLGL_Ckysh(unittest.TestCase):
    '''智慧护栏平台-安装线路管理模块-查看与审核测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\XLGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\AZXLGL\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://railbeta.starlinkware.com/")
        time.sleep(2)
        # 输入用户名
        cls.dr.find_element_by_id("username").send_keys("adminCK")
        time.sleep(1)
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Douniu2918")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(2)
        # 点击安装线路管理菜单
        cls.dr.find_element_by_xpath("/html/body/div[2]/ul/li[5]/ul/li").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_AZXLGL_Ckysh')
    def test_ZHHL_AZXLGL_Ckysh(self):
        '''安装线路管理模块-查看与审核测试用例'''
        # 输入路段名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路段名称"]').send_keys('马影河大道')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击查看与审核按钮
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/button[1]').click()
        time.sleep(2)
        # 选择审核状态：审核通过
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[3]/div/div[2]/div[4]/div[2]/div/div/input').click()
        time.sleep(1)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[3]/div/div[2]/div[4]/div[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[3]/div/div[2]/div[4]/div[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[3]/div/div[2]/div[4]/div[2]/div/div/input')\
            .send_keys(Keys.ENTER)
        # 点击提交
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[7]/div[3]/div/div[2]/div[5]/div/div/button').click()
        time.sleep(1)
        # 获取查询结果，保存在变量里
        p = self.dr.find_element_by_xpath('//p[@class="el-message__content"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '操作成功', '审核失败')
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_AZXLGL_Ckysh('test_ZHHL_AZXLGL_Ckysh'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-安装线路管理模块-查看与审核测试报告',
                  description='智慧护栏平台-安装线路管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../XLGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)