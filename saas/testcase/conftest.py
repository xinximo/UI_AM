#!/usr/bin/python3
# @Time    : 2021/3/15 3:44 下午
# @Author  : WangXin
import pytest

from saas.page.login_page import LoginPage


@pytest.fixture(scope="function")
def login():
    yield


