import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_AZZLGL(unittest.TestCase):
    '''车辆监控平台-安装资料管理模块-测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\AZZLGL\img"), img_name))

    # 启动测试用例方法
    @classmethod
    def setUpClass(cls):
        # 启动Chrome浏览器
        cls.dr=webdriver.Chrome()
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
        # 鼠标悬停在“客户资料管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[2]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(2)
        # 鼠标悬停在“安装资料管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击安装资料管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul').click()
        time.sleep(2)

    # 关闭测试用例方法
    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\AZZLGL\image\AZZLGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_AZZLGL_Cx')
    def test_CLJK_AZZLGL_Cx(self):
        '''安装资料管理模块-查询测试用例'''
        # #按IMEI精确查询
        # 输入IMEI号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索IMEI号"]').send_keys('861097041206321')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097041206321', '按IMEI查询安装信息失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

        # #按IMEI模糊查询
        # 输入IMEI号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索IMEI号"]').send_keys('182166')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '808029900182166', '按IMEI查询安装资料失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

        # #按安装点精确查询
        # 输入安装点
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索安装点"]').send_keys('安装测试')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 点击查看详情
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/a').click()
        time.sleep(2)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[2]/div[1]/div[4]/div[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '安装测试', '按安装点查询安装资料失败')
        time.sleep(2)
        # 关闭窗口
        self.dr.find_element_by_xpath(
            '//div[@aria-label="详情"]/div[2]/div[2]/div/div/button').click()
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

        # #按安装点模糊查询
        # 输入安装点
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索安装点"]').send_keys('测试')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(4)
        # 点击查看详情
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[6]/div/a').click()
        time.sleep(2)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[2]/div[1]/div[4]/div[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '安装测试', '按安装点查询安装资料失败')
        time.sleep(2)
        # 关闭窗口
        self.dr.find_element_by_xpath(
            '//div[@aria-label="详情"]/div[2]/div[2]/div/div/button').click()
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

        # #按安装时间查询
        # 点击安装时间按钮
        self.dr.find_element_by_xpath('//input[@placeholder="选择日期"]').click()
        time.sleep(1)
        # 点击月份
        self.dr.find_element_by_xpath('//div[@class="el-date-picker__header"]/span[2]').click()
        time.sleep(2)
        # 选中六月
        self.dr.find_element_by_xpath(
            '//table[@class="el-month-table"]/tbody/tr[2]/td[2]/div/a').click()
        time.sleep(2)
        # 选中十七日
        self.dr.find_element_by_xpath(
            '//table[@class="el-date-table"]/tbody/tr[4]/td[4]/div/span').click()
        time.sleep(2)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(4)
        # # 获取页面标签，保存到变量
        # div = self.dr.find_element_by_xpath(
        #     '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(div, '2020-06-17 10:33:02', '按安装时间查询安装资料失败')
        # time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_AZZLGL_Fy')
    def test_CLJK_AZZLGL_Fy(self):
        '''安装资料管理模块-分页显示测试用例'''
        # #按50条/页
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
        time.sleep(5)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(5)

        # #按500条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(7)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(3)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath('//div[@class="pagingChild"]/div/div/button[2]').click()
        time.sleep(3)
        # 点击上一页
        self.dr.find_element_by_xpath('//div[@class="pagingChild"]/div/div/button[1]').click()
        time.sleep(3)
        # 点击任意一页（5页）
        self.dr.find_element_by_xpath('//div[@class="pagingChild"]/div/div/ul/li[5]').click()
        time.sleep(3)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/span/div/input').send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        # 获取到输入页码框，并输入页码号“8”
        self.dr.find_element_by_xpath(
            '//div[@class="pagingChild"]/div/div/span/div/input').send_keys('8')
        time.sleep(2)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//div[@class="el-pagination is-background"]').click()
        time.sleep(3)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(3)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_AZZLGL_Ckxq')
    def test_CLJK_AZZLGL_Ckxq(self):
        '''安装资料管理模块-查看详情测试用例'''
        # 查看详情
        self.dr.find_element_by_link_text('查看详情').click()
        time.sleep(2)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[1]/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '详情', '查看详情失败')
        time.sleep(2)
        # 关闭窗口
        self.dr.find_element_by_xpath(
            '//div[@aria-label="详情"]/div[2]/div[2]/div/div/button').click()
        time.sleep(2)

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_AZZLGL('test_CLJK_AZZLGL_Cx'))
    testunit.addTest(MyTestCase_CLJK_AZZLGL('test_CLJK_AZZLGL_Fy'))
    testunit.addTest(MyTestCase_CLJK_AZZLGL('test_CLJK_AZZLGL_Ckxq'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-安装资料管理模块-测试报告',
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
