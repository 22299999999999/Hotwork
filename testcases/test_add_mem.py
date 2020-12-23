from time import sleep

import pytest
from selenium import webdriver

from page.basepage import BasePage
from page.main import MainPage


class TestAddmem:
    def setup_class(self):
        # 实例变量，可以在类的其他方法中调用
        self.index_main = MainPage()

    # 通讯录添加成员
    @pytest.mark.parametrize("name,acctid,phone,expected", [("name13", "username13", "13000000009", "name13"),
                                                            ("name14", "username15", "13000000010", "name14")])
    def test_add_mem_from_cont(self, name, acctid, phone, expected):
        # 1、跳转到通讯录，2、在通讯录页面点添加成员，跳转到成员页面3、添加成员 4、添加成员后自动跳转到通讯录页面  5、断言
        user_list = self.index_main.goto_con().goto_add_mem().add_mem(name, acctid, phone).get_user_list()
        assert expected in user_list

    # 首页添加成员
    @pytest.mark.parametrize("name,acctid,phone,expected", [("name13", "username13", "13000000009", "name13"),
                                                            ("name14", "username15", "13000000010", "name14")])
    def test_add_mem(self, name, acctid, phone, expected):
        # 1、首页点添加成员，跳到添加成员页面，2、添加成员  3、添加成员后自动跳转到通讯录页面  4、断言
        user_list = self.index_main.goto_add_mem().add_mem(name, acctid, phone).get_user_list()
        assert expected in user_list

    @pytest.mark.parametrize("part,parent_part,expected", [("513", "test_com", "513"), ("514", "test_com", "514")])
    def test_add_part(self, part, parent_part, expected):
        part_list = self.index_main.goto_con().goto_part(part, parent_part).get_part()
        sleep(1)
        assert expected in part_list

    def teardown(self):
        self.index_main.back_main()
