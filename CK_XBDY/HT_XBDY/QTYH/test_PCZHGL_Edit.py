import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_PCZHGL_Edit(unittest.TestCase):
    '''车辆监控平台-PC账户管理模块-编辑测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\PCZHGL\img"), img_name))

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
        cls.dr.find_element_by_id("password").send_keys("Ck19920308")
        time.sleep(1)
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        time.sleep(1)
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“后台系统管理”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[HT_XBDY]/div/div[HT_XBDY]/div/div/ul/li[5]')
        ActionChains(cls.dr).move_to_element(link).perform()
        # self.dr.implicitly_wait(5)
        time.sleep(1)
        # 鼠标悬停在“PC账户管理”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击PC账户管理菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[2]/ul').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\QTYH\image\PCZHGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_PCZHGL_Edit1')
    def test_CLJK_PCZHGL_Edit1(self):
        '''PC账户管理模块-编辑测试用例-状态：正常'''
        # 输入用户账户
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的用户账号"]').send_keys('纬希智能测试')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[6]/div/button[3]').click()
        time.sleep(2)
        # 修改用户账户
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户账号"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户账号"]').send_keys('纬希智能测试001')
        time.sleep(2)
        # 修改用户名
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('纬希智能测试001')
        time.sleep(2)
        # 修改手机号
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户手机号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入用户手机号"]').send_keys('13333333333')
        time.sleep(2)
        # 修改邮箱
        self.dr.find_element_by_xpath('//input[@placeholder="请输入邮箱"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入邮箱"]').send_keys('123@qq.com')
        time.sleep(2)
        # 选择证件类型（身份证）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择证件类型"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择证件类型"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择证件类型"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 修改证件号码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入证件号码"]').send_keys('420902199901011234')
        time.sleep(2)
        # 选择角色等级（安装人员）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择角色等级"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择角色等级"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择角色等级"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 选择状态（正常）
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[8]/div/label[HT_XBDY]/span[HT_XBDY]/span').click()
        time.sleep(2)
        # 选择地图展示位置（湖北省）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择您的地址"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择您的地址"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择您的地址"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 管辖客户默认
        # 点击提交
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[3]/div/button[HT_XBDY]').click()
        time.sleep(5)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '纬希智能测试001', '编辑PC账户失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除所有条件"]').click()
        time.sleep(2)

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_PCZHGL_Edit2')
    def test_CLJK_PCZHGL_Edit2(self):
        '''PC账户管理模块-编辑测试用例-状态：锁定'''
        # 输入用户账户
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的用户账号"]').send_keys('纬希智能测试001')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 点击编辑
        self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[6]/div/button[3]').click()
        time.sleep(2)
        # 修改用户账户
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户账号"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户账号"]').send_keys('纬希智能测试')
        time.sleep(2)
        # 修改用户名
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('纬希智能测试')
        time.sleep(2)
        # 修改手机号
        self.dr.find_element_by_xpath('//input[@placeholder="请输入用户手机号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入用户手机号"]').send_keys('13333333322')
        time.sleep(2)
        # 修改邮箱
        self.dr.find_element_by_xpath('//input[@placeholder="请输入邮箱"]').clear()
        self.dr.find_element_by_xpath('//input[@placeholder="请输入邮箱"]').send_keys('123@qq.com')
        time.sleep(2)
        # 选择证件类型（身份证）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择证件类型"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择证件类型"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择证件类型"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 修改证件号码
        self.dr.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入证件号码"]').send_keys('420902199901011444')
        time.sleep(2)
        # 选择角色等级（安装人员）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择角色等级"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择角色等级"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择角色等级"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 选择状态（锁定）
        self.dr.find_element_by_xpath(
            '//form[@class="el-form"]/div[8]/div/label[2]/span[HT_XBDY]/span').click()
        time.sleep(2)
        # 选择地图展示位置（湖北省）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择您的地址"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择您的地址"]').send_keys(Keys.DOWN)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择您的地址"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 管辖客户默认
        # 点击提交
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[3]/div/div[3]/div/button[HT_XBDY]').click()
        time.sleep(5)
        # 输入用户账户
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的用户账号"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入需要搜索的用户账号"]').send_keys('纬希智能测试')
        time.sleep(1)
        # 点击查询
        self.dr.find_element_by_xpath('//button[@title="搜索"]').click()
        time.sleep(2)
        # 获取页面元素，保存到变量
        div = self.dr.find_element_by_xpath(
            '//table[@class="el-table__body"]/tbody/tr[HT_XBDY]/td[2]/div').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(div, '纬希智能测试', '编辑PC账户失败')
        time.sleep(1)
        # 点击清除
        self.dr.find_element_by_xpath('//button[@title="清除所有条件"]').click()
        time.sleep(2)
        # 关闭PC账户管理界面
        self.dr.find_element_by_xpath('//*[@id="tab-/userManage"]/span[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_PCZHGL_Edit('test_CLJK_PCZHGL_Edit1'))
    testunit.addTest(MyTestCase_CLJK_PCZHGL_Edit('test_CLJK_PCZHGL_Edit2'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-PC账户管理模块-编辑测试报告',
                  description='车辆监控平台-PC账户管理模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../LSTZ/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)