from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os


class MyTestCase_CLJK_KHXXGL_Cx(unittest.TestCase):
    '''车辆监控平台-客户信息管理模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_CLJK\KHXXGL\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\KHXXGL\img"), img_name))

    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
        # 最大化浏览器
        cls.dr.maximize_window()
        # 输入登录网址
        cls.dr.get("https://ebeta.starlinkware.com/")
        time.sleep(2)
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
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“客户信息管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[1]/ul/li')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击客户信息管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[1]/ul/li').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\KHXXGL\image1\KHXXGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Cx')
    def test_CLJK_KHXXGL_Cx(self):
        '''客户信息管理模块-查询测试用例'''
        # #按客户名称精确查询
        # 输入客户信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').send_keys('陈凯测试')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div=self.dr.find_element_by_xpath('//div[@class="cell el-tooltip"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '陈凯测试', '按客户名称精确查询失败')
        time.sleep(2)
        # 点击清除查询条件按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        '''按客户名称模糊查询'''
        # 输入客户信息
        self.dr.find_element_by_class_name('el-input__inner').send_keys('陈')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath('//div[@class="cell el-tooltip"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '陈凯测试', '按客户名称模糊查询失败')
        time.sleep(2)
        # 点击清除查询条件按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        '''按状态查询-状态：正常'''
        # 点击状态按钮
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的状态"]').click()
        time.sleep(2)
        # 切换正常状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 选中正常状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[2]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '正常', '按正常状态查询失败')
        time.sleep(2)

        '''按状态查询-状态：锁定'''
        # 点击状态按钮
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的状态"]').click()
        time.sleep(2)
        # 切换锁定状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 选中锁定状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[2]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '锁定', '按锁定状态查询失败')

        '''按状态查询-状态：注销'''
        # 点击状态按钮
        self.dr.find_element_by_xpath('//input[@placeholder="请选择需要搜索的状态"]').click()
        time.sleep(2)
        # 切换注销状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的状态"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 选中注销状态
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择需要搜索的状态"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[2]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '注销', '注销状态查询失败')
        time.sleep(2)
        # 点击清空搜索条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Fy')
    def test_CLJK_KHXXGL_Fy(self):
        '''客户信息管理模块-分页测试用例'''
        '''按50条/页'''
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按50条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        '''按200条/页'''
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        '''按500条/页'''
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        '''按20条/页'''
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 点击清空搜索条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        '''上下页切换操作'''
        # 点击下一页
        self.dr.find_element_by_xpath('//button[@class="btn-next"]').click()
        time.sleep(2)
        # 点击上一页
        self.dr.find_element_by_xpath('//button[@class="btn-prev"]').click()
        time.sleep(2)
        # 点击任意一页（3页）
        self.dr.find_element_by_xpath('//ul[@class="el-pager"]/li[3]').click()
        time.sleep(2)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//span[@class="el-pagination__jump"]/div/input').send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        # 获取到输入页码框，并输入页码号“4”
        self.dr.find_element_by_xpath(
            '//span[@class="el-pagination__jump"]/div/input').send_keys('4')
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//div[@class="el-pagination is-background"]').click()
        time.sleep(2)
        # 点击清空搜索条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHZLGL_Khscx')
    def test_CLJK_KHZLGL_Khscx(self):
        '''客户资料管理模块-客户树查询测试用例'''
        # 输入客户树查询条件
        self.dr.find_element_by_xpath('//input[@placeholder="请选择客户"]').send_keys('陈凯测试')
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[6]/div[2]/div[1]/i').click()
        time.sleep(4)
        # 选中客户信息
        self.dr.find_element_by_xpath('//a[@title="陈凯测试"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '陈凯测试', '按客户树查询失败')
        time.sleep(2)
        # 点击清空搜索条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Cx('test_CLJK_KHXXGL_Cx'))
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Cx('test_CLJK_KHXXGL_Fy'))
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Cx('test_CLJK_KHZLGL_Khscx'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-客户信息管理模块-查询测试报告',
                  description='车辆监控平台-客户信息管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # fp = open('../KHXXGL/image1/result1.html', 'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner(stream=fp, title='车辆监控平台-UI自动化测试报告', description='客户信息管理模块-测试用例执行情况')
    # # 执行测试用例
    # # runner = unittest.TextTestRunner()
    # runner.run(testunit)