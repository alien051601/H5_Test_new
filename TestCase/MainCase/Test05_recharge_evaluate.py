from time import sleep
import unittest
from Test02_Login import Login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Recharge_Evaluate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化Login（）方法
        Recharge_Evaluate.recharge = Login()
        # 获取Login()里面获得的excel的数据
        cls.username = Recharge_Evaluate.recharge.username
        cls.password = Recharge_Evaluate.recharge.password
        cls.real_name = Recharge_Evaluate.recharge.real_name
        cls.pc_id = Recharge_Evaluate.recharge.pc_id
        cls.bank_code=Recharge_Evaluate.recharge.bank_code
        cls.bank_mobile=Recharge_Evaluate.recharge.bank_mobile
        cls.invitcode=Recharge_Evaluate.recharge.invitcode
        # 获取Login()里面的driver
        cls.driver = Recharge_Evaluate.recharge.driver
        # 执行Login()里面的登录方法
        Recharge_Evaluate.recharge.test_1_login()

        print(cls.username,cls.password,cls.real_name,cls.pc_id,cls.bank_code,cls.bank_mobile,cls.invitcode)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.quit()


    # 从产品详情页面，进入充值页面
    # unittest.skip('充值成功')
    def test_1_recharge(self):
        print('test_1_recharge开始执行')
        driver = Recharge_Evaluate.recharge.driver
        # 点击----赢计划 页面---进入----新手标---标签列表
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/a[2]/span').click()
        sleep(2)
        # span[1]代表进入第一个标签页
        driver.find_element_by_xpath('/html/body/p[2]/span[6]').click()
        sleep(2)

        # 点击赢计划C的第一标
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[2]').click()
        sleep(2)

        # 输入购买金额---选择--同意出借协议
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[3]/input').send_keys(200)
        sleep(1)
        driver.find_element_by_class_name('am-ucheck-icons').click()
        sleep(1)

        # 点击----加入
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[6]').click()
        sleep(2)

        try:
            recharge_info = driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[5]').text
            self.assertEqual(recharge_info, '账户余额不足')

        except:
            print('账户余额为零时，购买产品的提示错误')

        try:
            # 点击充值按钮---进入充值页面
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[2]/i[2]').click()
        except:
            print('没有捕获到产品详情页面------充值按钮的元素')
            driver.quit()
        sleep(2)


    # 进入充值详情页面，输入充值金额和密码
    # unittest.skip('充值成功之后')
    def test_2_recharge(cls):
        print('test_2_recharge_开始执行')
        driver = cls.driver
        driver.implicitly_wait(20)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        try:
            locator = (By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/input')
            print('---------------1---------------')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            sleep(2)
            print('---------------2---------------')
            recharge_num = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/input')
            print('---------------3---------------')
            recharge_num.send_keys('50000')
            sleep(2)
        except:
            print('Error05_02---没有成功加载充值页面')
            driver.close()

        # 点击发送验证码，并点击--立即充值
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[3]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[2]/input').send_keys('666666')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]').click()
        sleep(2)

        # 在充值成功页面里面，捕获充值结果
        try:
            locator = (By.XPATH, '/html/body/div[2]/p[2]')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            sleep(2)
            recharge_result = driver.find_element_by_xpath('/html/body/div[2]/p[2]').text
            cls.assertEqual(recharge_result, '充值成功')
            sleep(2)
        except:
            print('Error05_03---充值失败')
            driver.close()

        # 点击 前往加入
        driver.find_element_by_xpath('/html/body/div[2]/p[4]/a').click()
        sleep(10)

    # 充值成功之后，再次进入产品详情页面，弹出风险评测页面
    def test_3_evaluate(cls):
        driver = cls.driver
        # # span[3]代表进入第三个标签页
        # driver.find_element_by_xpath('/html/body/p[2]/span[3]').click()
        # sleep(2)
        #
        # # 点击赢计划C的第一标
        # driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[2]').click()
        # sleep(2)

        # 输入购买金额---选择--同意出借协议
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[3]/input').send_keys(200)
        sleep(1)
        driver.find_element_by_class_name('am-ucheck-icons').click()
        sleep(1)

        # 点击----加入
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[6]').click()
        sleep(2)

        # 获取风险评测的弹框
        try:
            locator = (By.XPATH, '/html/body/div[9]/div/div/div/p[2]')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[9]/div/div/div/p[2]').click()
            sleep(2)

        except:
            print('Error05_04---未获得风险评测弹窗')
            driver.close()

        # 风险评测详情
        try:
            locator = (By.XPATH, '/html/body/div[2]/div[1]/p[2]/label/span/i[2]')
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            sleep(2)
            # 第一题
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第二题
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第三题
            driver.find_element_by_xpath('/html/body/div[2]/div[3]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第四题
            driver.find_element_by_xpath('/html/body/div[2]/div[4]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第五题
            driver.find_element_by_xpath('/html/body/div[2]/div[5]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第六题
            driver.find_element_by_xpath('/html/body/div[2]/div[6]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第七题
            driver.find_element_by_xpath('/html/body/div[2]/div[7]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第八题
            driver.find_element_by_xpath('/html/body/div[2]/div[8]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第九题
            driver.find_element_by_xpath('/html/body/div[2]/div[9]/p[2]/label/span/i[2]').click()
            sleep(1)
            # 第十题
            driver.find_element_by_xpath('/html/body/div[2]/div[10]/p[2]/label/span/i[2]').click()
            sleep(1)

        except:
            print('Error05_05---未成功加载风险评测页面')
            driver.close()

        # 点击提交评测
        driver.find_element_by_xpath('/html/body/div[2]/p[21]').click()
        sleep(2)
        '/html/body/div[2]/p[21]'
        evaluate_type = driver.find_element_by_xpath('//*[@id="pxlx"]/i').text
        print('您的风险评测的类型为：', evaluate_type)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/p[2]').click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()



