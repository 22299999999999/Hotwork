import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver is None:
            # 注解，不是赋值操作。用作ide的类型提示
            base_driver: WebDriver
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.__cookies_login()
        else:
            self.driver = base_driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def __cookies_login(self):
        with open("../data3.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def setup(self):
        pass

    def teardown(self):
        self.driver.quit()

    def find(self, way, key=None):
        if key is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_element(*way)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_element(by=way, value=key)

    def finds(self, way, key=None):
        if key is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*way)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=way, value=key)
