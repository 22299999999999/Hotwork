from time import sleep
import faker

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWework:

    def test_add(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)
        with open("../data3.yaml", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[class=ww_operationBar] a:nth-child(2)').click()
        sleep(2)
        self.driver.find_element(By.ID, 'username').send_keys("name4")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("username4")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("13000000004")
        sleep(2)
        self.driver.find_element(By.XPATH, '//form[@class="js_member_editor_form"]/div[3]/a[2]').click()
