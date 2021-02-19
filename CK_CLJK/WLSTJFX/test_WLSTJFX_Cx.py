import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_WLSTJFX_Cx(unittest.TestCase):
    '''车辆监控平台-物流锁统计分析模块-查询测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\WLSTJFX\img"), img_name))

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
        # 点击物流锁统计分析菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[5]/ul').click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\DQTJFX\image\WLSTJFX_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_WLSTJFX_Cx')
    def test_CLJK_WLSTJFX_Cx(self):
        '''物流锁统计分析模块-查询测试用例'''
        # #按车牌号精确查询
        # 输入车牌号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号"]').send_keys('物流锁测试')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '物流锁测试', '按车牌号查询物流锁失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(3)

        # #按车牌号模糊查询
        # 输入车牌号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号"]').send_keys('物流锁')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '物流锁测试', '按车牌号查询物流锁失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(3)

        # #按IMEI精确查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的IMEI"]').send_keys('000014143382110')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '000014143382110', '按IMEI查询物流锁失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(3)

        # #按IMEI模糊查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的IMEI"]').send_keys('2110')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '000014143382110', '按IMEI查询物流锁失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除搜索条件"]').click()
        time.sleep(3)

        # #按锁状态查询（闭锁）
        # 选择锁状态
        self.dr.find_element_by_xpath('//input[@placeholder="请选择锁状态"]').click()
        time.sleep(1)
        # 选中闭锁
        self.dr.find_element_by_xpath('//input[@placeholder="请选择锁状态"]').send_keys(Keys.DOWN)
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择锁状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # # 获取页面元素，保存到变量
        # div = self.dr.find_element_by_xpath(
        #     '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # # 判断预期结果与实际结果是否一致
        # self.assertEqual(div, '闭锁', '按闭锁状态查询物流锁失败')
        # time.sleep(1)

        # #按锁状态查询（开锁）
        # 选择锁状态
        self.dr.find_element_by_xpath('//input[@placeholder="请选择锁状态"]').click()
        time.sleep(1)
        # 选中开锁
        self.dr.find_element_by_xpath('//input[@placeholder="请选择锁状态"]').send_keys(Keys.DOWN)
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择锁状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(3)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '开锁', '按开锁状态查询物流锁失败')
        time.sleep(1)

    @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_WLSTJFX_Fy')
    def test_CLJK_WLSTJFX_Fy(self):
        '''物流锁统计分析模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按50条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.ENTER)
        time.sleep(7)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.ENTER)
        time.sleep(15)

        # #按500条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.ENTER)
        time.sleep(15)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[2]/div/div/input')\
            .send_keys(Keys.ENTER)
        time.sleep(8)

        # #上下页切换操作
        # 点击下一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/button[2]').click()
        time.sleep(7)
        # 点击上一页
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/button[1]').click()
        time.sleep(7)
        # 点击任意一页（5页）
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/ul/li[5]').click()
        time.sleep(7)
        # 获取到输入页码框，并清理掉当前页码号
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[3]/div/input')\
            .send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        # 获取到输入页码框，并输入页码号“8”
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[3]/div/div[2]/div/div/span[3]/div/input')\
            .send_keys('8')
        time.sleep(2)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath('//div[@class="el-pagination is-background"]').click()
        time.sleep(5)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_WLSTJFX_Cx('test_CLJK_WLSTJFX_Cx'))
    testunit.addTest(MyTestCase_CLJK_WLSTJFX_Cx('test_CLJK_WLSTJFX_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-物流锁统计分析模块-查询测试报告',
                  description='车辆监控平台-物流锁统计分析模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../WLSTJFX/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)