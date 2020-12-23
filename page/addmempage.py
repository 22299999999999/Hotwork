import pytest
from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.contpage import ContPage


class AddMem(BasePage):
    location_username = (By.ID, 'username')
    location_acctid = (By.ID, 'memberAdd_acctid')
    location_phone = (By.ID, 'memberAdd_phone')
    location_add = (By.XPATH, '//form[@class="js_member_editor_form"]/div[3]/a[2]')

    def add_mem(self, username, acctid, phone):
        """添加成员
        :return:
        """
        self.find(self.location_username).send_keys(username)
        self.find(self.location_acctid).send_keys(acctid)
        self.find(self.location_phone).send_keys(phone)
        self.find(self.location_add).click()
        return ContPage(self.driver)
