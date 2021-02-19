import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_SBJK(unittest.TestCase):
    '''车辆监控平台-设备监控模块-测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\SBJK\img"), img_name))

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
        # 鼠标悬停在“设备监控中心”链接上
        link = cls.dr.find_element_by_xpath(
            '//div[@class="happy-scroll-content"]/div/ul/li[3]')
        ActionChains(cls.dr).move_to_element(link).perform()
        # cls.dr.implicitly_wait(5)
        time.sleep(1)
        # 鼠标悬停在“设备监控”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[1]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击设备监控菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[1]/ul').click()
        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\SBJK\image\SBJK_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBJK_Cx')
    def test_CLJK_SBJK_Cx(self):
        '''设备监控模块-查询测试用例'''
        # #按客户树查询
        # 选择客户树查询
        self.dr.find_element_by_id('ztree_1_span').click()
        time.sleep(8)

        # #按车牌号查询
        # 输入查询条件车牌号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').send_keys('鄂A98V88')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//div[@class="custSearch"]/div[3]/span').click()
        time.sleep(3)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '鄂A98V88', '按车牌号查询设备列表失败')
        time.sleep(2)
        # 清空查询条件框
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').clear()
        time.sleep(2)

        # #按IMEI查询
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').send_keys('808029900170161')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//div[@class="custSearch"]/div[3]/span').click()
        time.sleep(3)
        # 获取页面标签，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '鄂A98V88', '按IMEI查询设备列表失败')
        time.sleep(2)
        # 清空查询条件框
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').clear()
        time.sleep(2)

        # 点击查询按钮
        self.dr.find_element_by_xpath('//div[@class="custSearch"]/div[3]/span').click()
        time.sleep(6)
        # 点击行驶分类
        self.dr.find_element_by_xpath(
            '//div[@class="el-radio-group"]/label[2]/span[1]/span').click()
        time.sleep(7)
        # 点击停止分类
        self.dr.find_element_by_xpath(
            '//div[@class="el-radio-group"]/label[3]/span[1]/span').click()
        time.sleep(7)
        # 点击离线分类
        self.dr.find_element_by_xpath(
            '//div[@class="el-radio-group"]/label[4]/span[1]/span').click()
        time.sleep(7)
        # 点击刷新界面
        self.dr.find_element_by_xpath(
            '//*[@id="tab-/deviceMonitor"]/span[1]/span[2]/i').click()
        time.sleep(4)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBJK_Fy')
    def test_CLJK_SBJK_Fy(self):
        '''设备监控模块-分页测试用例'''
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
        time.sleep(7)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(2)
        # 下一页
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(2)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(7)

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
        time.sleep(7)

        # # #上下页切换操作
        # # 点击下一页
        # self.dr.find_element_by_xpath('//button[@class="btn-next"]').click()
        # time.sleep(5)
        # # 点击上一页
        # self.dr.find_element_by_xpath('//button[@class="btn-prev"]').click()
        # time.sleep(5)
        # # 点击任意一页（4页）
        # self.dr.find_element_by_xpath(
        # '//*[@id="app"]/div/div[6]/div[2]/div[5]/div/div/ul/li[4]').click()
        # time.sleep(3)
        # # 获取到输入页码框，并清理掉当前页码号
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[6]/div[2]/div[5]/div/div/span[3]/div/input').send_keys(Keys.BACK_SPACE)
        # time.sleep(2)
        # # 获取到输入页码框，并输入页码号“8”
        # self.dr.find_element_by_xpath(
        #     '//*[@id="app"]/div/div[6]/div[2]/div[5]/div/div/span[3]/div/input').send_keys('8')
        # time.sleep(2)
        # # 点击空白处，切换到当前页码
        # self.dr.find_element_by_xpath('//*[@id="app"]/div/div[6]/div[2]/div[1]/div').click()
        # time.sleep(5)
        # 点击刷新界面
        self.dr.find_element_by_xpath(
            '//*[@id="tab-/deviceMonitor"]/span[1]/span[2]/i').click()
        time.sleep(3)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBJK_Gj')
    def test_CLJK_SBJK_Gj(self):
        '''设备监控模块-查看轨迹测试用例'''
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').send_keys('863013182137614')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//div[@class="custSearch"]/div[3]/span').click()
        time.sleep(4)
        # 点击轨迹按钮
        self.dr.find_element_by_xpath('//span[@title="轨迹"]').click()
        time.sleep(3)
        # 获取页面标签，保存到变量
        span = self.dr.find_element_by_xpath(
            '//*[@id="tab-/track"]/span[1]/span[1]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '轨迹追踪', '打开轨迹追踪界面失败')
        time.sleep(2)
        # 点击关闭轨迹追踪界面
        self.dr.find_element_by_xpath('//*[@id="tab-/track"]/span[2]').click()
        time.sleep(2)
        # 清空查询条件框
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').clear()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBJK_Ckxq')
    def test_CLJK_SBJK_Ckxq(self):
        '''设备监控模块-查看详情测试用例'''
        # 输入IMEI
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的车牌号或IMEI"]').send_keys('863013182137614')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//div[@class="custSearch"]/div[3]/span').click()
        time.sleep(4)
        # 勾选设备
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div[4]/div/div[3]/table'
            '/tbody/tr/td[1]/div/label/span/span').click()
        time.sleep(2)
        # 点击详情按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div/div[3]'
            '/table/tbody/tr/td[10]/div/span[2]').click()
        time.sleep(2)
        # 获取页面标签，保存到变量
        span = self.dr.find_element_by_xpath('//*[@id="tab-first"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '设备信息', '查看详情失败')
        time.sleep(2)
        # 点击关闭详情窗口
        self.dr.find_element_by_xpath(
            '//div[@class="el-dialog__wrapper dialogDetailMonitor"]/div/div[1]/button').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_SBJK_Dw')
    def test_CLJK_SBJK_Dw(self):
        '''设备监控模块-定位测试用例'''
        # 点击定位
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div/div[3]/table'
            '/tbody/tr/td[10]/div/span[1]').click()
        time.sleep(3)

if __name__=='__main__':
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_SBJK('test_CLJK_SBJK_Cx'))
    testunit.addTest(MyTestCase_CLJK_SBJK('test_CLJK_SBJK_Fy'))
    testunit.addTest(MyTestCase_CLJK_SBJK('test_CLJK_SBJK_Gj'))
    testunit.addTest(MyTestCase_CLJK_SBJK('test_CLJK_SBJK_Ckxq'))
    testunit.addTest(MyTestCase_CLJK_SBJK('test_CLJK_SBJK_Dw'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-设备监控模块-查询测试报告',
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