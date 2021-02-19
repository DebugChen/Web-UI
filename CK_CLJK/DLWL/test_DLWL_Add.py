import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_CLJK_DLWL_Add(unittest.TestCase):
    '''车辆监控平台-地理围栏模块-新增测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\DLWL\img"), img_name))

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
        cls.dr.find_element_by_id("password").send_keys("Xd0020110")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(2)
        # 鼠标悬停在“设备监控中心”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div/ul/li[3]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“地理围栏菜单”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击地理围栏菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul').click()
        time.sleep(5)

    # 关闭测试用例方法
    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\SBZLGL\image\DLWL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_DLWL_Add')
    def test_CLJK_DLWL_Add(self):
        '''地理围栏模块-新增测试用例'''
        # 点击车辆监控中心
        self.dr.find_element_by_id('ztree_1_span').click()
        time.sleep(6)
        # 定位城市
        self.dr.find_element_by_xpath(
            '//input[@placeholder="可输入城市进行定位"]').send_keys('硚口区')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//*[@id="pane-first"]/div/div/div').click()
        time.sleep(2)
        # 输入围栏名称
        self.dr.find_element_by_xpath(
            '//*[@id="pane-first"]/div/form/div[1]/div/div/input').send_keys('测试围栏11-23-2')
        time.sleep(1)

        # 选择画圆
        self.dr.find_element_by_xpath(
            '//*[@id="monitorMap"]/div[2]/div/div/div[1]/div/label[1]/span[1]/span').click()
        time.sleep(1)
        # 绘制护栏位置
        A1 = self.dr.find_element_by_xpath(
            '//*[@id="mymap"]/div[1]/div/div[1]/canvas[2]')
        A2 = self.dr.find_element_by_xpath(
            '//*[@id="mymap"]/div[1]/div/div[1]/canvas[2]')
        # 对元素进行拖动操作
        ActionChains(self.dr).drag_and_drop(A1, A2).perform()
        time.sleep(1)
        # 点击创建围栏按钮
        self.dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[3]/div/button').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        p = self.dr.find_element_by_xpath('//div[@role="alert"]/p').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '操作成功', '新增围栏失败')
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_DLWL_Add('test_CLJK_DLWL_Add'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-地理围栏模块-新增测试报告',
                  description='车辆监控平台-地理围栏模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # 定义测试报告存放路径
    # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)