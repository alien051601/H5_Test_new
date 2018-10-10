from read_excel import *
from utilities.settings import *
from utilities.common_method import *


class Login(CommonMethod):

    def __init__(self):
        super(Login).__init__()
        self.c = CommonMethod()

        # 如下的属性，方便其他类调用的时候使用
        self.driver = self.c.driver

        # 点击首页的---【我的】----【注册/登录】
        my_account_css = read_css_path(63)
        print(my_account_css)
        self.c.click_element_by_css(my_account_css)
        sleep(1)
        register_login_css = read_css_path(64)
        self.c.click_element_by_css(register_login_css)
        sleep(1)

        # 获取登录信息的css元素以及登录账号信息
        mobile_login_css = read_css_path(88)
        pw_login_css = read_css_path(89)
        pw_visible_login_css = read_css_path(90)
        submit_login_css = read_css_path(91)
        self.login_mobile, self.login_pw = read_login_data(row_num_real)

        # 输入登录信息并提交
        self.c.input_element_by_css(mobile_login_css,self.login_mobile)
        sleep(1)
        self.c.input_element_by_css(pw_login_css, self.login_pw)
        sleep(1)
        # self.c.driver.find_element_by_css_selector(pw_visible_login_css).click()
        self.c.click_element_by_css(pw_visible_login_css)
        sleep(1)
        self.c.click_element_by_css(submit_login_css)
        sleep(3)


    def test_1_inter_borrow_detail(self):
        # 点击---【出借】
        buy_css = read_css_path(62)
        self.c.wait_element_click_by_css(buy_css)
        sleep(1)

        # 获取出借页面---【下拉列表按钮】&【第三个标的类型】的css
        show_all_type = read_css_path(70)
        updown_page_3 = read_css_path(73)

        # 点击标的类型下拉框,选中第三个类型
        self.c.click_element_by_css(show_all_type)
        sleep(1)
        self.c.click_element_by_css(updown_page_3)
        sleep(1)

        # 选中第三个类型的第一个标的，进入详情
        win_3_1_borrow_name_css = read_css_path(77)
        self.c.wait_element_click_by_css(win_3_1_borrow_name_css)
        sleep(1)

        # 点击---【立即加入】
        buy_right_now_css = read_css_path(79)
        self.c.wait_element_click_by_css(buy_right_now_css)
        sleep(1)

    def test_2_buy_process(self):

        # 进入到产品详情并点击立即加入
        self.test_1_inter_borrow_detail()

        # 购买过程
        buy_amount_buy_css = read_css_path(80)
        self.c.wait_element_input_by_css(buy_amount_buy_css, '46000')
        sleep(2)

        # 同意三个协议
        agree_on_buy_css = read_css_path(81)
        self.c.click_element_by_css(agree_on_buy_css)
        sleep(1)

        # 点击---【确认购买】
        buy_assure_buy =read_css_path(82)
        self.c.click_element_by_css(buy_assure_buy)
        sleep(2)

        # 获取点击购买之后可能出现的错误提示（余额不足等）
        error_info_buy_css = read_css_path(83)
        error_info_buy = self.c.driver.find_element_by_css_selector(error_info_buy_css).text
        print(error_info_buy)
        sleep(2)

        # 捕获结果页面
        result_buy_buy_css = read_css_path(72)
        result = self.c.driver.find_element_by_css_selector(result_buy_buy_css).text
        print('购买结果为：', result)
        return result

if __name__ == "__main__":
    l = Login()






