# -*- coding:utf-8 -*- #
# @time 2021-03-10 11:55
# author:pengda
from time import sleep

import allure
import pytest


@pytest.mark.op_login
@allure.feature('登陆op')
class TestDemoOp:

    @allure.story('登陆成功')
    @pytest.mark.parametrize(['username', 'password'], [('admin@gdp.com', '12345678')])
    def test_login_op(self, go_into_url, username, password):
        text = go_into_url.jump_and_login(username, password)
        sleep(5)

