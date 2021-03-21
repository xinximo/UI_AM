# -*- coding:utf-8 -*- #
# @time 2021-03-10 11:52
# author:pengda
from selenium.webdriver.common.by import By

from saas.base_page import SaasBasePage
from saas.page.main_page import MainPage


class LoginPage(SaasBasePage):
    _location_login = By.CSS_SELECTOR, '.btn-login a[href="/login"]'
    _location_username = (By.CSS_SELECTOR, 'input[name="accountName"]')
    _location_password = (By.CSS_SELECTOR, 'input[name="password"]')
    _location_login_click = By.CSS_SELECTOR, '.input-set button'
    _username = 'zhanghao@growingio.com'
    _password = 'growingio'
    _location_main = (By.CSS_SELECTOR, ".platform-app-logo-wrapper")

    def jump_and_login(self):
        self.wait_click(self._location_login)
        self.find_click(self._location_login)
        self.send_keys(self._location_username, self._username)
        self.send_keys(self._location_password, self._password)
        # self.send_keys(self._location_username, username)
        # self.send_keys(self._location_password, password)
        self.find_click(self._location_login_click)
        return MainPage(self.driver)

    def back_main(self):
        self.find(self._location_main).click()
