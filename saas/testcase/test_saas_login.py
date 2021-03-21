# -*- coding:utf-8 -*- #
# @time 2021-03-10 11:55
# author:pengda
from time import sleep

import allure
import pytest


from saas.page.login_page import LoginPage
from saas.page.main_page import MainPage


@pytest.mark.saas_login
@allure.feature('登陆saas')
class TestDemoSaas:
    def setup_class(self):
        self.main = LoginPage()

    def teardown_class(self):
        self.main.quit()

    @allure.story('登陆成功')
    @pytest.mark.parametrize(['username', 'password'], [('zhanghao@growingio.com', 'growingio')])
    def test_login_saas(self, username, password):
        r = self.main.jump_and_login(username, password).get_index_assert_text()
        assert 'GrowingIO' == r
        sleep(3)