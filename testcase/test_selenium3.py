from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.add import Add
from common.loginpage import LoginPage


class TestWework:

    def test_add(self, myfixture):
        log = LoginPage(myfixture)
        log.login()
        add = Add(myfixture)
        add.add_mem("na20", "ac20", "13000000020")
