from time import sleep
from read_excel import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class Base():

    def __init__(self):
        mobileEmulation = {'deviceName': 'iPhone 6 Plus'}

        # 设置浏览器的配置信息
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        options.add_argument('disable-infobars')  # 设置成用户自己的数据目录

        # 设置chrome浏览器的driver
        path = 'D:\Program Files\Google\Chrome\Application\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=path)

        # 设置浏览器显示的尺寸大小
        self.driver.set_window_size(420, 820)
        sleep(2)

        # 设置浏览器左上角在屏幕中的位置
        self.driver.set_window_position(x=700, y=20)
        sleep(2)

        # 在浏览器中打开目标网址
        self.driver.get(url=API_TEST_BASE_URL)
        print('使用Chrome打开目标网址')
        sleep(2)
        # 读取登录的用户名和密码
        row_num = row_num_real
        self.username, self.password = read_login_data(row_num)


    # 打开首页之后-----点击【xpath】地址的按钮
    def click_first_xpath(self, xpath):
        driver = self.driver
        print('开始登陆操作')
        driver.find_element_by_xpath(xpath).click()
        sleep(1)

    # 打开首页之后-----点击【css】地址的按钮
    def click_first_css(self, css):
        driver = self.driver
        print('开始登陆操作')
        driver.find_element_by_css_selector(css).click()
        sleep(1)



# b = Base()
# show_all_type = read_css_path(70)
# updown_page_3 = read_css_path(73)
#
# # 点击标的类型下拉框
# b.driver.find_element_by_css_selector(show_all_type).click()
# sleep(1)
# b.driver.find_element_by_css_selector(updown_page_3).click()
# sleep(2)


# start_position = b.driver.find_element_by_css_selector(win_NOC1_type_css)
# end_position = b.driver.find_element_by_css_selector(win_new_type_css)
#
# action = ActionChains(b.driver)
# print("-------0-------------")
# action.click_and_hold(start_position).release(end_position).perform()
# sleep(2)






