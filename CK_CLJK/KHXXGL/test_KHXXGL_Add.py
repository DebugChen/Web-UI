import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains


class MyTestCase_CLJK_KHXXGL_Add(unittest.TestCase):
    '''车辆监控平台-客户信息管理模块-新增测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
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
        cls.dr.find_element_by_xpath("/html/body/div[2]/ul/li[1]/ul/li").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\KHXXGL\image1\KHXXGL_Add.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Add1')
    def test_CLJK_KHXXGL_Add1(self):
        '''客户信息管理模块-新增测试用例-状态:正常'''
        # 点击右侧客户树节点
        self.dr.find_element_by_xpath('//span[@class="node_name"]').click()
        time.sleep(2)
        # 点击新增客户按钮
        self.dr.find_element_by_xpath('//div[@class="btnArrList"]/button[1]').click()
        time.sleep(2)
        # 输入客户名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入客户名称，不可包含数字和特殊字符"]').send_keys('测试客户A')
        time.sleep(1)
        # 输入联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('测试客户A')
        time.sleep(1)
        # 输入联系电话
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系电话"]').send_keys('13367889870')
        time.sleep(1)
        # 输入联系地址
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系地址，不超过50个字符"]').send_keys('武汉市')
        time.sleep(1)
        # 输入安装账号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入安装账号"]').send_keys('测试客户A')
        time.sleep(1)
        # 状态默认：正常
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[6]/div/label[1]').click()
        time.sleep(2)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[3]/div/button[1]').click()
        time.sleep(2)
        # 点击清除查询条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)
        # 输入客户信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').send_keys('测试客户A')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '测试客户A', '新增正常状态客户失败')
        time.sleep(1)
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[6]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '正常', '新增正常状态客户失败')
        time.sleep(2)
        # 点击清除查询条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KHXXGL_Add2')
    def test_CLJK_KHXXGL_Add2(self):
        '''客户信息管理模块-新增测试用例-状态:锁定'''
        # 点击右侧客户树节点
        self.dr.find_element_by_xpath('//span[@class="node_name"]').click()
        time.sleep(2)
        # 点击新增客户按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 输入客户名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入客户名称，不可包含数字和特殊字符"]').send_keys('测试客户B')
        time.sleep(1)
        # 输入联系人
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系人"]').send_keys('测试客户B')
        time.sleep(1)
        # 输入联系电话
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系电话"]').send_keys('13367889871')
        time.sleep(1)
        # 输入联系地址
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入联系地址，不超过50个字符"]').send_keys('武汉市')
        time.sleep(1)
        # 输入安装账号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入安装账号"]').send_keys('测试客户B')
        time.sleep(1)
        # 选择状态：锁定
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[6]/div/label[2]').click()
        time.sleep(2)
        # 点击提交按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[3]/div/button[1]').click()
        time.sleep(2)
        # 点击清除查询条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)
        # 输入客户信息
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的客户名称"]').send_keys('测试客户B')
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div1 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[1]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div1, '测试客户B', '新增锁定状态客户失败')
        time.sleep(1)
        # 获取页面元素，保存到变量
        div2 = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[6]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div2, '锁定', '新增锁定状态客户失败')
        time.sleep(2)
        # 点击清除查询条件
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

if __name__=='__main__':
    # 执行测试用例
    # unittest.main()
    # 构造测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Add('test_CLJK_KHXXGL_Add1'))
    testunit.addTest(MyTestCase_CLJK_KHXXGL_Add('test_CLJK_KHXXGL_Add2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-客户信息管理模块-新增测试报告',
                  description='车辆监控平台-客户信息管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)