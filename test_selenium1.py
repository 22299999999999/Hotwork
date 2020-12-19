import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        # self.driver.quit()
        pass

        # def test_a(self):
        # by id
        # self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        # by name
        # self.driver.find_element(By.NAME,'wd').send_keys("霍格沃兹测试学院")
        # css name
        self.driver.find_element(By.CSS_SELECTOR, '[name=wd]').send_keys("霍格沃兹测试学院")

        # by xpath
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # css  id
        # self.driver.find_element(By.CSS_SELECTOR,'#su').click()
        # self.driver.find_element(By.CSS_SELECTOR,'[id=su]').click()


# 复用浏览器
class TestFuyong:
    def test_abc(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element(By.ID, 'menu_contacts').click()
        print(driver.get_cookies())
        sleep(5)
        print(driver.find_element(By.CSS_SELECTOR, '#member_list td:nth-child(5)/span'))


# 使用cookie登录
class TestWework:
    def test_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853324263676'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853324263676'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324949206547'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '8992pUzOYyi0bm7O_wGAoP89WFV3_gO9SrFvvJpsiT45Sc2K-VYpxayDwYCNKkll'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9627475'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'CwoGfZyYDgzppTw0UCj28k4ZvAtlBfRzIbQoB648DWf9c7eoMu_N-cKV3QcHJOv051faAiwSUXkvSGg-JIOmTVpfu_gH1Hg-QH9KkI7eKbB86zs0NC_yo3IFDY_o5dO99Ny32jX47JYrsGdNLS2B2IA_D5v2IOD7G4NSeADWmwlLOA8I3E0U55EhvqLwKYA0xRfEGNLZIrpr1znobgfxPbQ9ugXeJ9lcTjujdv-Fkvz0CWNJO0tCEH9ZpaVZWwCh3bo-oiRFRzZL5UTThYbQFw'},
            {'domain': '.qq.com', 'expiry': 1608213866, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1608238080, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '74g2eap'},
            {'domain': '.qq.com', 'expiry': 1608300218, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.394729292.1608206547'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '1389740033205414'},
            {'domain': '.qq.com', 'expiry': 1671285818, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.508887416.1608106467'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1639642465, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '1990477298'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1610805827, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '4dc3c4a174c0d2dd00260f1b1ce44cbc627ae73dbdfc5800fb5029add3b95d20'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'hISAKtj2GC'},
            {'domain': '.qq.com', 'expiry': 1609568551, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '852501385@qq.com'}
        ]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element(By.ID, 'menu_contacts').click()
        sleep(4)


class TestLogin:
    # 获取cookie，序列化后存入yaml文件内
    def test_get_cookies(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookie = driver.get_cookies()
        print(cookie)
        with open("./data3.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    # 使用序列化cookie的方法进行登录
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("data3.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        sleep(4)
        driver.find_element(By.CSS_SELECTOR, '[class=ww_operationBar] a:nth-child(2)').click()
        sleep(2)
        driver.find_element(By.ID, 'username').send_keys("name13")
        driver.find_element(By.ID, 'memberAdd_acctid').send_keys("username13")
        driver.find_element(By.ID, 'memberAdd_phone').send_keys("13000000009")
        driver.find_element(By.XPATH, '//form[@class="js_member_editor_form"]/div[3]/a[2]').click()
        sleep(4)
        assert driver.find_element(By.CSS_SELECTOR, '[class=js_mod_party_name]').is_displayed()
