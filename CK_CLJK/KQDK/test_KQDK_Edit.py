import os
from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MyTestCase_CLJK_KQDK_Edit(unittest.TestCase):
    '''车辆监控平台-考勤打卡模块-编辑考勤测试集'''

    # 自定义截图方法
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
       """
        # os.path.abspath(r"E:\UIZDH\CK_CLJK\KQDK\img")截图存放路径
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(
            r"E:\UIZDH\CK_CLJK\KQDK\img"), img_name))

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
        # 输入密码
        cls.dr.find_element_by_id("password").send_keys("Xd0020110")
        # 输入验证码
        cls.dr.find_element_by_id("code").send_keys("1234")
        # 点击登录按钮
        cls.dr.find_element_by_xpath('//input[@value="登录"]').click()
        time.sleep(3)
        # 鼠标悬停在“设备监控中心”链接上
        link = cls.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[1]/div/div/ul/li[3]')
        ActionChains(cls.dr).move_to_element(link).perform()
        time.sleep(1)
        # 鼠标悬停在“考勤打卡”链接上
        link2 = cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul')
        ActionChains(cls.dr).move_to_element(link2).perform()
        time.sleep(2)
        # 点击考勤打卡菜单
        cls.dr.find_element_by_xpath('/html/body/div[2]/ul/li[3]/ul').click()
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        # # 报错截图
        # cls.dr.get_screenshot_as_file(
        #     'C:\\Users\starlinkware\PycharmProjects\\CK_CLJK\PCZHGL\image\PCZHGL_Cx.png')
        # 关闭浏览器
        cls.dr.quit()

    # @unittest.skip('跳过用例')
    # 装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img('001')方法
    @BeautifulReport.add_test_img('test_CLJK_KQDK_Edit')
    def test_CLJK_KQDK_Edit(self):
        '''考勤打卡模块-编辑考勤测试用例'''
        # 点击编辑考勤
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div[1]/div/div[1]/div/ul/li[2]/div/div[2]').click()
        time.sleep(3)
        # 修改考勤名称
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入考勤名称"]').clear()
        self.dr.find_element_by_xpath(
            '//input[@placeholder="请输入考勤名称"]').send_keys('测试考勤12-9-11')
        time.sleep(1)
        # 修改考勤对象（车辆监控中心）
        self.dr.find_element_by_xpath('//*[@id="ztree_1_span"]').click()
        time.sleep(1)
        # 修改考勤时间（上班时间）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择上班时间"]').send_keys('09:00:00')
        time.sleep(1)
        # 修改考勤时间（下班时间）
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').click()
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys(Keys.BACK_SPACE)
        self.dr.find_element_by_xpath('//input[@placeholder="请选择下班时间"]').send_keys('18:00:00')
        time.sleep(1)
        # 滚动进度条
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div[1]/div/div[2]/div').click()
        time.sleep(1)
        # 获取需要滚动至可见元素
        target = self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div[1]/div/div[1]/div/ul/li[1]/div[2]/div[5]/button[1]')
        time.sleep(1)
        # 拖动到可见的元素去
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(1)
        # 点击绘制地图
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div[1]/div/div[1]/div'
            '/ul/li[1]/div[2]/div[4]/div[2]/button[1]').click()
        time.sleep(3)
        # 绘制护栏位置
        A1 = self.dr.find_element_by_xpath('//canvas[@class="amap-labels"]')
        A2 = self.dr.find_element_by_xpath('//canvas[@class="amap-labels"]')
        # 对元素进行拖动操作
        ActionChains(self.dr).drag_and_drop(A1, A2).perform()
        time.sleep(1)
        # 点击保存
        self.dr.find_element_by_xpath(
            '//*[@id="app"]/div/div[6]/div[2]/div[1]/div/div[1]/div/ul/li[1]/div[2]/div[5]/button[1]').click()
        time.sleep(1)
        # 获取页面元素，保存到变量
        p = self.dr.find_element_by_xpath('//p[@class="el-message__content"]').text
        # 判断预期结果与实际结果是否一致
        self.assertEqual(p, '提交成功', '编辑考勤失败')
        time.sleep(1)

if __name__ == '__main__':
    # unittest.main()
    # 组装测试套件
    testunit = unittest.TestSuite()
    # 添加测试用例
    testunit.addTest(MyTestCase_CLJK_KQDK_Edit('test_CLJK_KQDK_Edit'))
    # 定义测试报告
    runner = BeautifulReport(testunit)
    runner.report(filename='车辆监控平台-考勤打卡模块-编辑考勤测试报告',
                  description='车辆监控平台-考勤打卡模块-测试用例执行情况',
                  report_dir='report',
                  theme='theme_default')
    # # 定义测试报告存放路径
    # # fp = open('../KHXXGL/image1/result2.html', 'wb')
    # # 定义测试报告
    # # runner = HTMLTestRunner(stream=fp, title='车辆监控平台UI自动化测试报告', description='客户信息管理模块测试用例执行情况')
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(testunit)