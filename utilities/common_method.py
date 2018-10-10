from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from base import Base


class CommonMethod(Base):

    def __init__(self):
        super(CommonMethod,self).__init__()

    # 判断元素是否存在，通过element_xpath
    def is_element_exit_xpath(self, element_xpath):
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_xpath(element_xpath)
            return flag

        except:
            print('获取的元素xpath不存在:', element_xpath)
            flag = False
            return flag

    # 判断元素是否存在，通过element_css
    def is_element_exit_css(self, element_css):
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_css_selector(element_css)
            return flag

        except:
            print('获取的元素css不存在:', element_css)
            flag = False
            return flag


    # 判断元素是否可以操作，通过element_xpath
    def is_element_enabled_xpath(self, element_xpath):
        flag = True
        driver = self.driver
        try:
            result = driver.find_element_by_xpath(element_xpath).is_enabled()
            if result == True:
                return flag

        except:
            print('获取的元素xpath不能操作:', element_xpath)
            flag = False
            return flag

        # 判断元素是否可以操作，通过element_xpath
    def is_element_enabled_css(self, element_css):
        flag = True
        driver = self.driver

        result = driver.find_element_by_css_selector(element_css).is_enabled()
        if result:
            return flag
        else:
            print('获取的元素css不能操作:', element_css)
            flag = False
            return flag

    # 等待元素出现，直到可以操作，通过element_xpath
    def wait_element_by_xpath(self, element_xpath):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.XPATH, element_xpath)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，xpath地址为:', element_xpath)
            driver.quit()

        if self.is_element_enabled_xpath(element_xpath):
            sleep(2)
            return flag
        else:
            flag = False
            print('20s之后等待的元素不能操作,元素的xpath:',element_xpath)
            self.driver.quit()
            return flag

    # 等待元素出现，直到可以操作，通过element_css
    def wait_element_by_css(self, element_css):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.CSS_SELECTOR, element_css)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，css地址为:', element_css)
            driver.quit()

        if self.is_element_enabled_css(element_css):
            sleep(2)
            return flag

        else:
            flag = False
            print('20s之后等待的元素不能操作,元素的css:',element_css)
            self.driver.quit()
            return flag

    # 等待元素出现，并点击，通过element_xpath
    def wait_element_click_by_xpath(self, element_xpath):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.XPATH, element_xpath)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，xpath地址为:', element_xpath)
            driver.quit()

        if self.driver.find_element_by_xpath(element_xpath).is_enabled():
            sleep(1)
            self.driver.find_element_by_xpath(element_xpath).click()
            return flag
        else:
            flag = False
            print('20s之后等待的元素不能操作,元素的xpath:',element_xpath)
            self.driver.quit()
            return flag

    # 等待元素出现，并点击，通过element_css
    def wait_element_click_by_css(self, element_css):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.CSS_SELECTOR, element_css)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，clsss_css地址为:', element_css)
            driver.quit()

        if self.driver.find_element_by_css_selector(element_css).is_enabled():
            sleep(1)
            self.driver.find_element_by_css_selector(element_css).click()
            return flag
        else:
            flag = False
            print('20s之后等待的元素不能操作,元素的css:',element_css)
            self.driver.quit()
            return flag

    # 等待元素出现，并点击，通过class_name
    def wait_element_click_by_class_name(self, element_class_name):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.CSS_SELECTOR, element_class_name)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，clsss_name地址为:', element_class_name)
            driver.quit()

        if self.driver.find_element_by_class_name(element_class_name).is_enabled():
            sleep(1)
            self.driver.find_element_by_class_name(element_class_name).click()
            return flag
        else:
            flag = False
            print('20s之后等待的元素不能操作,class_name:',element_class_name)
            self.driver.quit()
            return flag


    # 等待元素出现，并输入内容，通过element_xpath
    def wait_element_input_by_xpath(self, element_xpath, input_info):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.XPATH, element_xpath)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，xpath地址为:', element_xpath)
            driver.quit()

        if self.driver.find_element_by_xpath(element_xpath).is_enabled():
            sleep(1)
            self.driver.find_element_by_xpath(element_xpath).send_keys(input_info)
            return flag
        else:
            flag = False
            print('20s之后等待的元素不能操作,xpath地址为：',element_xpath)
            self.driver.quit()
            return flag

    # 等待元素出现，并输入内容，通过element_css
    def wait_element_input_by_css(self, element_css, input_info):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)

        locator = (By.CSS_SELECTOR, element_css)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，css地址为:',element_css)
            driver.quit()

        if self.is_element_enabled_css(element_css):
            sleep(1)
            self.driver.find_element_by_css_selector(element_css).send_keys(input_info)
            return flag
        else:
            flag = False
            print('20s之后等待的元素不能操作,css地址为：', element_css)
            self.driver.quit()
            return flag

    # 等待元素出现，并获取元素text的值
    def wait_element_get_text_by_css(self, element_css):
        flag = True
        driver = self.driver
        # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
        driver.implicitly_wait(20)
        locator = (By.CSS_SELECTOR, element_css)
        try:
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located(locator))
        except:
            print('Error_等待20s之后，未加载到等待的元素，css地址为:', element_css)
            driver.quit()

        element_text = driver.find_element_by_css_selector(element_css).text
        if element_text:
            print('获取到元素text的值为：', element_text)
            return element_text
        else:
            flag = False
            print('Error_元素的text的值不存在,css地址为：', element_css)
            self.driver.quit()
            return flag

    # 根据CSS的路径，点击元素
    def click_element_by_css(self, element_css):
        if self.driver.find_element_by_css_selector(element_css).is_enabled():
            self.driver.find_element_by_css_selector(element_css).click()

        else:
            print('元素CSS的路径错误，无法点击：', element_css)
            self.driver.quit()

    # 根据xpath的路径，点击元素
    def click_element_by_xpath(self, element_xpath):
        if self.driver.find_element_by_xpath(element_xpath).is_enabled():
            self.driver.find_element_by_xpath(element_xpath).click()

        else:
            print('元素xpath的路径错误，无法点击：', element_xpath)
            self.driver.quit()

    # 根据class_name的路径，点击元素
    def click_element_by_class_name(self, element_class_name):
        if self.driver.find_element_by_class_name(element_class_name).is_enabled():
            self.driver.find_element_by_class_name(element_class_name).click()

        else:
            print('元素class_name的路径错误，无法点击：', element_class_name)
            self.driver.quit()

    # 根据id的路径，点击元素
    def click_element_by_id(self, element_id):
        if self.driver.find_element_by_id(element_id).is_enabled():
            self.driver.find_element_by_id(element_id).click()

        else:
            print('元素class_name的路径错误，无法点击：', element_id)
            self.driver.quit()

    # 根据CSS的路径，输入内容
    def input_element_by_css(self, element_css, input_info):
        if self.driver.find_element_by_css_selector(element_css).is_enabled():
            self.driver.find_element_by_css_selector(element_css).send_keys(input_info)

        else:
            print('元素CSS的路径错误,无法输入内容：', element_css)
            self.driver.quit()

    # 根据xpath的路径，输入内容
    def input_element_by_xpath(self, element_xpath, input_info):
        if self.driver.find_element_by_xpath(element_xpath).is_enabled():
            self.driver.find_element_by_xpath(element_xpath).send_keys(input_info)
        else:
            print('元素xpath的路径错误,无法输入内容：', element_xpath)
            self.driver.quit()


# c = CommonMethod()
# first_xpath = '/html/body/div[1]/div/div[1]/p[2]/a[1]/span'
# c.wait_element_click_by_xpath(first_xpath)
#
# first_css = 'input[name="user_number_"]'
# c.wait_element_input_by_css(first_css, '18612345')
# sleep(3)
# c.driver.quit()
