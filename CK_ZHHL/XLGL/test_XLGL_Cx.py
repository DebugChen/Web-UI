import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_ZHHL_AZXLGL_Cx(unittest.TestCase):
    '''智慧护栏平台-安装线路管理模块-查询测试集'''

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
    @BeautifulReport.add_test_img('test_ZHHL_AZXLGL_Cx')
    def test_ZHHL_AZXLGL_Cx(self):
        '''安装线路管理模块-查询测试用例'''
        # #按路段名称精确查询
        # 输入路段名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路段名称"]').send_keys('谌家矾大道')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '谌家矾大道', '按路段名称查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按路段名称模糊查询
        # 输入路段名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路段名称"]').send_keys('谌')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '谌家矾大道', '按路段名称查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按路口名称精确查询（开始路口）
        # 输入路口名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路口名称"]').send_keys('朱家河大挢-谌家矾大道001')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '朱家河大挢-谌家矾大道001', '按路口名称查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按路口名称精确查询（结束路口）
        # 输入路口名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的路口名称"]').send_keys('朱家河大挢-谌家矾大道084')
        time.sleep(2)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[4]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '朱家河大挢-谌家矾大道084', '按路口名称查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

        # #按审核状态查询（安装进行）
        # 点击审核状态按钮
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').click()
        time.sleep(2)
        # 切换安装进行
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 定义变量，用于存放获取到的页面元素
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '安装进行', '按安装进行审核状态查询失败')
        time.sleep(2)

        # #按审核状态查询（审核通过）
        # 点击审核状态按钮
        self.dr.find_element_by_xpath('//input[@placeholder="请选择路段审核状态"]').click()
        time.sleep(2)
        # 切换审核通过
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 定义变量，用于存放获取到的页面元素
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '审核通过', '按审核通过审核状态查询失败')
        time.sleep(2)

        # #按审核状态查询（安装完成）
        # 点击审核状态按钮
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').click()
        time.sleep(2)
        # 切换安装完成
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 定义变量，用于存放获取到的页面元素
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '安装完成', '按安装完成审核状态查询失败')
        time.sleep(2)

        # #按审核状态查询（撤销路段）
        # 点击审核状态按钮
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').click()
        time.sleep(2)
        # 切换撤销路段
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择路段审核状态"]').send_keys(Keys.ENTER)
        time.sleep(1)
        # 点击查询按钮
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 定义变量，用于存放获取到的页面元素
        span = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[1]/td[5]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(span, '撤销路段', '按安装完成审核状态查询失败')
        time.sleep(2)
        # 点击清空按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_AZXLGL_Fy')
    def test_ZHHL_AZXLGL_Fy(self):
        '''安装线路管理模块-分页测试用例'''
        # #按50条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按50条分页显示）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按200条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按200条分页显示）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按500条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按500条分页显示）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        # #按20条/页
        # 点击分页显示
        self.dr.find_element_by_xpath('//input[@placeholder="请选择"]').click()
        time.sleep(1)
        # 下一页
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.DOWN)
        time.sleep(1)
        # 回撤（按20条分页显示）
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请选择"]').send_keys(Keys.ENTER)
        time.sleep(2)

        # #上下页切换操作
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
        time.sleep(1)
        # 点击空白处，切换到当前页码
        self.dr.find_element_by_xpath(
            '//div[@class="el-pagination is-background"]').click()
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath('//button[@title="清空搜索条件"]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_AZXLGL_Cx('test_ZHHL_AZXLGL_Cx'))
    testunit.addTest(MyTestCase_ZHHL_AZXLGL_Cx('test_ZHHL_AZXLGL_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='智慧护栏平台-安装线路管理模块-查询测试报告',
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