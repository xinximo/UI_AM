# # -*- coding:utf-8 -*- #
# # @time 2021-03-10 11:56
# # author:pengda
# import pytest
#
# from basepage.base_page import BasePage
#
# @pytest.mark.skip
# @pytest.fixture(scope='session')
# def init_browser():
#     init_driver = BasePage()
#     yield init_driver
#     init_driver.close_browser()
#
# @pytest.mark.skip
# # 解决用例添加标签后出现的警告
# def pytest_configure(config):
#     """
#     将添加的标签名放到marker_list中
#     """
#     marker_list = ['saas_login', 'op_login']
#     for markers in marker_list:
#         config.addinivalue_line('markers', markers)
