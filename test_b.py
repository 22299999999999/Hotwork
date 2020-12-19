from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Selenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_home(self):
        # self.driver.find_element_by_xpath("//section/ul/li[2]/a").click()
        self.driver.find_element(By.ID, "kw").send_keys("selenium测试")
        self.driver.find_element(By.ID, "su").click()
        # 直接等待
        sleep(3)
        # 显式等待
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'cur-tab')))
        print("hello python")
