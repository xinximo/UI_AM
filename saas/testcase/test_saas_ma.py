#!/usr/bin/python3
# @Time    : 2021/3/15 3:44 下午
# @Author  : WangXin

from datetime import datetime
from time import sleep

import allure
import pytest
from saas.page.login_page import LoginPage
from saas.page.main_page import MainPage

error_time = datetime.now().strftime('%F %T')
true_time = datetime.now().strftime('%Y%m%d%H%M%S')


@allure.feature("新建弹窗")
class TestCreateWindows:
    def setup_method(self):
        self.main = LoginPage()


    @pytest.mark.parametrize("url, images, windows_name, res", [("http://www.baidu.com",
                                                                 "https://img2.tapimg.com/bbcode/images/c9ce1cb2861dca1eadc94ab73d351f84.jpg",
                                                                 f"UI自动化{true_time}", f"UI自动化{true_time}")])
    @allure.story("新建弹窗_新建成功")
    def test_new_windows_success(self, url, images, windows_name, res):
        # 新建弹窗测试用例成功

        r = self.main.jump_and_login().goto_marketing_auto().goto_marketing_activity().goto_channel_in_app_messages_ready_online_success(
            url, images, windows_name)
        assert r in res
        sleep(3)


    @pytest.mark.parametrize("url, images, windows_name, res", [("http://www.baidu.com",
                                                                 "https://img2.tapimg.com/bbcode/images/c9ce1cb2861dca1eadc94ab73d351f84.jpg",
                                                                 f"UI自动化{error_time}", "名称只支持中英文数字和空格以及 _-\/()（）!")])
    @allure.story("新建弹窗_弹窗名称存在异常字符")
    def test_new_windows_error(self, url, images, windows_name, res):
        # 新建弹窗测试用例失败
        r = self.main.jump_and_login().goto_marketing_auto().goto_marketing_activity().goto_channel_in_app_messages_ready_online_error(
            url, images, windows_name)
        assert r in res
        sleep(3)

    def teardown_method(self):
        # 测试完毕返回主页
        # self.main.back_main()
        self.main.quit_browser()

    """
    执行测试用例并生成测试报告:
    cd saas
    pytest -sv testcase/test_saas_ma.py --alluredir ./report --clean-alluredir
    allure serve ./report
    """
