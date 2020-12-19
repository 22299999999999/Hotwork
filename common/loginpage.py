import yaml
from common.page import Page
from selenium import webdriver


class LoginPage(Page):
    def get_cookies(self, filename):
        path = "../" + filename
        # "../data3.yaml"
        with open(path, encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            return cookies

    def login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.get_cookies("data3.yaml")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
