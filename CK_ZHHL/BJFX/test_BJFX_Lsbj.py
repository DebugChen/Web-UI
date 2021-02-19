import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_ZHHL_BJFX_Lsbj(unittest.TestCase):
    '''城市基础设施监测平台-报警分析模块-历史报警测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_ZHHL\BJFX\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_ZHHL\BJFX\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr = webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("http://172.30.1.200:7070/")
        # 输入用户名
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys("chenkai")
        time.sleep(0.5)
        # 输入密码
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("Xd0020110")
        time.sleep(0.5)
        # 输入验证码
        cls.dr.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys("1111")
        time.sleep(0.5)
        # 点击登录按钮
        cls.dr.find_element_by_class_name('loginEvent').click()
        time.sleep(2)
        # 鼠标悬停在“数据中心”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[1]/li')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 点击报警分析菜单
        cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/div/div[2]/div/div[2]/div/p').click()
        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Lsbj')
    def test_ZHHL_BJFX_Lsbj(self):
        '''报警分析模块-历史报警测试用例'''
        # 输入IMEI号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI"]').send_keys('861097041599261')
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(4)
        # 点击历史报警
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr/td[9]/div/div/button[1]').click()
        time.sleep(5)
        # 获取查询结果，保存在变量里
        span = self.dr.find_element_by_xpath(
            '//div[@class="un-play-button"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '轨迹播放', '打开历史报警失败')
        # 点击任意历史报警数据
        self.dr.find_element_by_xpath(
            '//div[@class="histroy-alarm-contain-list"]/div/div[1]/div[2]/table/tbody/tr[1]').click()
        time.sleep(1)
        # 获取查询结果，保存在变量里
        span = self.dr.find_element_by_xpath('//div[@class="address"]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '湖北省武汉市硚口区韩家墩街道武汉博济智汇园', '定位历史报警位置失败')

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Lsbj_Fy')
    def test_ZHHL_BJFX_Lsbj_Fy(self):
        '''报警分析模块-历史报警分页查询测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/'
            'div[2]/ul/div/div[1]/div/div[1]').click()
        time.sleep(0.5)
        # 选中50条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/'
            'div[2]/ul/div/div[1]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(10)

        # #按100条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/'
            'div[2]/ul/div/div[1]/div/div[1]').click()
        time.sleep(1)
        # 选中100条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/'
            'div[2]/ul/div/div[1]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(15)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/'
            'ul/div/div[1]/div/div[1]').click()
        time.sleep(1)
        # 选中20条/页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]'
            '/ul/div/div[1]/div/div[2]/ul[2]/li[1]').click()
        time.sleep(6)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/li[7]').click()
        time.sleep(5)
        # 点击上一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/li[1]').click()
        time.sleep(5)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/li[4]').click()
        time.sleep(5)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/div/div[2]/input') \
            .send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        # 获取到输入页码框，并输入页码号“5”
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/div/div[2]/input') \
            .send_keys('5')
        time.sleep(0.5)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]').click()
        time.sleep(5)
        # 刷新报警分析界面
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[1]/div[2]/img').click()
        time.sleep(5)
        # 点击关闭历史报警窗口
        self.dr.find_element_by_xpath(
            '//img[@src="/img/closeWindow.ccf2d9a9.svg"]').click()
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_BJFX_Lsbj('test_ZHHL_BJFX_Lsbj'))
    testunit.addTest(MyTestCase_ZHHL_BJFX_Lsbj('test_ZHHL_BJFX_Lsbj_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-报警分析模块-历史报警测试报告',
                  description='城市基础设施监测平台-报警分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../ZZGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)