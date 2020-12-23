# from base.base import Base
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.basepage import BasePage


class ContPage(BasePage):
    _location_contpage = (By.CSS_SELECTOR, '#menu_contacts')
    _location_addmem = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    location_addmem = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    location_gotopart = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    location_addpart = (By.CSS_SELECTOR, ".js_create_party")
    location_partname = (By.CSS_SELECTOR, '[name=name]')
    location_select_part = (By.CSS_SELECTOR, '.js_toggle_party_list')
    location_parent_part = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div/div/ul/li/a')
    location_button = (By.CSS_SELECTOR, '[d_ck=submit]')
    location_partlist = (By.CSS_SELECTOR, ".jstree-anchor")

    def goto_add_mem(self):
        from page.addmempage import AddMem

        """点击添加成员按钮，进入添加成员页面
        :return:
        """
        sleep(5)
        # WebDriverWait(self.driver,9).until(expected_conditions.element_to_be_clickable(*self._location_addmem))
        self.find(self._location_addmem).click()
        return AddMem(self.driver)

    def get_user_list(self):
        """获取成员列表
        :return:
        """
        self.driver.refresh()
        user_list = self.finds(self.location_addmem)
        # 列表推导式
        user_list1 = []
        for i in user_list:
            user_list1.append(i.text)
        return user_list1

    def goto_part(self, part, parent_part):
        """添加部门
        :return:
        """
        self.find(self.location_gotopart).click()
        self.find(self.location_addpart).click()
        self.find(self.location_partname).send_keys(part)
        self.find(*self.location_select_part).click()
        sleep(2)
        self.find(*self.location_parent_part).click()
        sleep(1)
        self.find(*self.location_button).click()
        return ContPage(self.driver)

    def get_part(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(self.location_partlist))
        part_list = self.finds(self.location_partlist)
        # 列表推导式
        part_list1 = []
        for i in part_list:
            part_list1.append(i.text)
        print(part_list1)
        sleep(1)

        return part_list1
