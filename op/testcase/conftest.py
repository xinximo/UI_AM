# -*- coding:utf-8 -*- #
# @time 2021-03-11 10:38
# author:pengda
import pytest


@pytest.fixture(scope='module')
def go_into_url(init_browser):
    yield init_browser.open_url('http://qa-cdp.growingio.cn/')

