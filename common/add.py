from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.page import Page


class Add(Page):
    contascts = (By.ID, 'menu_contacts')
    addpage = (By.CSS_SELECTOR, '[class=ww_operationBar] a:nth-child(2)')
    name = (By.ID, 'username')
    acct = (By.ID, 'memberAdd_acctid')
    phone = (By.ID, 'memberAdd_phone')
    savepage = (By.XPATH, '//form[@class="js_member_editor_form"]/div[3]/a[2]')
    change = (By.CSS_SELECTOR, '[class=js_mod_party_name]')

    def enter_con(self):
        self.find_element(*self.contascts).click()

    def add_page(self):
        self.find_element(*self.addpage).click()

    def set_name(self, name):
        self.find_element(*self.name).send_keys(name)

    def set_acct(self, acct):
        self.find_element(*self.acct).send_keys(acct)

    def set_phone(self, phone):
        self.find_element(*self.phone).send_keys(phone)

    def click_save(self):
        self.find_element(*self.savepage).click()

    def add_mem(self, name, acct, phone):
        self.enter_con()
        sleep(2)
        self.add_page()
        self.set_name(name)
        self.set_acct(acct)
        self.set_phone(phone)
        sleep(2)
        self.click_save()

    def is_success(self):
        try:
            self.find_element(*self.change)
        except NoSuchElementException:
            return False
        else:
            return True
