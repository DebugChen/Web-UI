import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_ZHHL_BJFX_Cx(unittest.TestCase):
    '''城市基础设施监测平台-报警分析模块-查询测试集'''

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
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Cx')
    def test_ZHHL_BJFX_Cx(self):
        '''报警分析模块-查询测试用例'''
        # #按IMEI精确查询
        # 输入IMEI号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI"]').send_keys('861097040964243')
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
            'div[1]/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097040964243', '按IMEI精确查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按IMEI模糊查询
        # 输入IMEI号
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入IMEI"]').send_keys('4243')
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
            'div[1]/div[2]/table/tbody/tr/td[1]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '861097040964243', '按IMEI模糊查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按所属路段精确查询
        # 输入所属路段
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入所属路段"]')\
            .send_keys('韩家墩街道古田五路')
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '韩家墩街道古田五路', '按所属路段精确查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按所属路段模糊查询
        # 输入所属路段
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入所属路段"]') \
            .send_keys('韩家墩')
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(2)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '韩家墩街道古田五路', '按所属路段模糊查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按报警类型查询（侧翻报警）
        # 选择报警类型
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[1]/li[3]/div/div[1]').click()
        # 选中报警类型：侧翻报警
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[1]/li[3]/div/div[2]/ul[2]/li[2]').click()
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="请选择报警类型"]').send_keys(Keys.DOWN)
        # time.sleep(1)
        # # 点击选中
        # self.dr.find_element_by_xpath(
        #     '//input[@placeholder="请选择报警类型"]').send_keys(Keys.ENTER)
        # time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(3)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '侧翻报警', '按侧翻报警类型查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按报警类型查询（拆卸报警）
        # 选择报警类型
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[1]/li[3]/div/div[1]').click()
        # 选中报警类型：拆卸报警
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[1]/li[3]/div/div[2]/ul[2]/li[3]').click()
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(3)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '拆卸报警', '按拆卸报警类型查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按报警类型查询（移动异常）
        # 选择报警类型
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[1]/li[3]/div/div[1]').click()
        # 选中报警类型：移动异常
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[1]/li[3]/div/div[2]/ul[2]/li[4]').click()
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(3)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
            '/div/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '移动异常', '按移动异常类型查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按报警时间查询
        # 选择报警时间段
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入报警时间"]').click()
        time.sleep(1)
        # 点击年份
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul[2]/'
            'li[1]/div/div[2]/div/div/div/div[1]/div[1]/span[3]/span[1]').click()
        time.sleep(1)
        # 选中2020年
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul[2]/'
            'li[1]/div/div[2]/div/div/div/div[1]/div[2]/span[1]/em').click()
        time.sleep(1)
        # 选中12月
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul[2]/'
            'li[1]/div/div[2]/div/div/div/div[1]/div[2]/span[12]/em').click()
        time.sleep(1)
        # 选中17日
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul[2]/'
            'li[1]/div/div[2]/div/div/div/div[1]/div[2]/span[19]/em').click()
        time.sleep(1)
        # 选中30日
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul[2]/'
            'li[1]/div/div[2]/div/div/div/div[1]/div[2]/span[32]/em').click()
        time.sleep(1)
        # 点击确认按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[1]/ul[2]/'
            'li[1]/div/div[2]/div/div/div/div[4]/button[3]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(6)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
            'div[1]/div[2]/table/tbody/tr[1]/td[5]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '2020-12-17 01:31:53', '按报警时间查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按解除报警方式查询（未解除）
        # 选择解除报警方式
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[2]/li[2]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中解除报警方式：未解除
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[2]/li[2]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(6)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '未解除', '按未解除解除报警方式查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按解除报警方式查询（自动解除）
        # 选择解除报警方式
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[2]/li[2]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中解除报警方式：自动解除
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[2]/li[2]/div/div[2]/ul[2]/li[3]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(6)
        # 获取查询结果，保存在变量里
        div = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/'
            'div/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '自动解除', '按自动解除解除报警方式查询失败')
        time.sleep(2)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

        # #按解除报警方式查询（手动解除）
        # 选择解除报警方式
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[2]/li[2]/div/div[1]/div/span').click()
        time.sleep(1)
        # 选中解除报警方式：手动解除
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/'
            'div[1]/ul[2]/li[2]/div/div[2]/ul[2]/li[4]').click()
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
        time.sleep(6)
        # 点击清除按钮
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(7)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_ZHHL_BJFX_Fy')
    def test_ZHHL_BJFX_Fy(self):
        '''报警分析模块-分页测试用例'''
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
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/div/div[2]/input')\
            .send_keys(Keys.BACK_SPACE)
        time.sleep(0.5)
        # 获取到输入页码框，并输入页码号“5”
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/ul/div/div[2]/input')\
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

if __name__=='__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_ZHHL_BJFX_Cx('test_ZHHL_BJFX_Cx'))
    testunit.addTest(MyTestCase_ZHHL_BJFX_Cx('test_ZHHL_BJFX_Fy'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='城市基础设施监测平台-报警分析模块-查询测试报告',
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