import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.addmempage import AddMem
from page.contpage import ContPage
from time import sleep


class MainPage(BasePage):
    _location_contpage = (By.CSS_SELECTOR, '#menu_contacts')
    _location_addpage = (By.CSS_SELECTOR, '.ww_indexImg_AddMember')
    location_mainpage = (By.ID, "menu_index")

    def goto_con(self):
        """进入通讯录页面
        :return:
        """
        sleep(4)
        self.find(self._location_contpage).click()
        return ContPage(self.driver)

    def goto_add_mem(self):
        """添加成员
        :return:
        """
        self.find(self._location_addpage).click()
        return AddMem(self.driver)

    def back_main(self):
        self.find(self.location_mainpage).click()
