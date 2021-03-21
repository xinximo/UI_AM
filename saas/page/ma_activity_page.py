#!/usr/bin/python3
# @Time    : 2021/3/15 3:04 下午
# @Author  : WangXin
from time import sleep

from selenium.webdriver.common.by import By

from saas.base_page import SaasBasePage


class MaActivityPage(SaasBasePage):
    _location_in_app_messages = By.CSS_SELECTOR, '[id="活动类型$Menu"]>li:nth-child(1)'
    _location_create_windows = By.CSS_SELECTOR, '.gio-ma-btn-small'
    _location_create_windows_web = By.CSS_SELECTOR, '.ma-create-modal__body>li:nth-child(1)'
    _location_create_windows_web_data_two = By.CSS_SELECTOR, '.ant-layout-content>div:nth-child(2)>.step-card'
    _location_create_windows_web_data_two_url = By.CSS_SELECTOR, '.gio-ma-input__content-prefix'
    _location_create_windows_web_data_three = By.CSS_SELECTOR, '.ant-layout-content>div:nth-child(3)>.step-card'
    _location_create_windows_web_data_images = By.CSS_SELECTOR, '.gio-ma-input__content'
    _location_create_windows_web_data_four = By.CSS_SELECTOR, '.ant-layout-content>div:nth-child(4)'
    _location_create_windows_web_data_save = By.CSS_SELECTOR, '.step-card__o-content button'
    _location_create_windows_web_data_submit = By.CSS_SELECTOR, '.gio-ma-btn-large'
    _location_create_windows_web_data_submit_name = By.CSS_SELECTOR, '.gio-ma-popover-content input'
    _location_create_windows_web_data_submit_sure = By.CSS_SELECTOR, '.RunButton__Wrapper-sc-159i7ry-0 button:nth-child(2)'
    _location_ready_online_success_res =By.CSS_SELECTOR, '.gio-ma-breadcrumb>span:nth-child(2) a'
    _location_ready_online_error_res = By.CSS_SELECTOR, '.ant-form-explain'

    def goto_channel_in_app_messages_ready_online_success(self, url, images, windows_name):
        """
        测试新建弹窗推送
        正常用例:新建成功
        """
        self.wait_click(self._location_in_app_messages)
        self.find_click(self._location_in_app_messages)
        self.wait_click(self._location_create_windows)
        self.find_click(self._location_create_windows)
        self.find_click(self._location_create_windows_web)
        self.find_click(self._location_create_windows_web_data_two)
        self.send_keys(self._location_create_windows_web_data_two_url, url)
        self.find_click(self._location_create_windows_web_data_three)
        self.send_keys(self._location_create_windows_web_data_images, images)
        self.find_click(self._location_create_windows_web_data_four)
        self.find_click(self._location_create_windows_web_data_save)
        sleep(1)
        self.find_click(self._location_create_windows_web_data_four)
        self.find_click(self._location_create_windows_web_data_submit)
        self.send_keys_clear(self._location_create_windows_web_data_submit_name, windows_name)
        self.find_click(self._location_create_windows_web_data_submit_sure)
        self.wait_click(self._location_ready_online_success_res)
        res = self.find(self._location_ready_online_success_res).text
        return res

    def goto_channel_in_app_messages_ready_online_error(self, url, images, windows_name):
        """
        测试新建弹窗推送
        异常用例:确认弹窗名称输入字符异常
        """
        self.wait_click(self._location_in_app_messages)
        self.find_click(self._location_in_app_messages)
        self.wait_click(self._location_create_windows)
        self.find_click(self._location_create_windows)
        self.find_click(self._location_create_windows_web)
        self.find_click(self._location_create_windows_web_data_two)
        self.send_keys(self._location_create_windows_web_data_two_url, url)
        self.find_click(self._location_create_windows_web_data_three)
        self.send_keys(self._location_create_windows_web_data_images, images)
        self.find_click(self._location_create_windows_web_data_four)
        self.find_click(self._location_create_windows_web_data_save)
        sleep(1)
        self.find_click(self._location_create_windows_web_data_four)
        self.find_click(self._location_create_windows_web_data_submit)
        self.send_keys_clear(self._location_create_windows_web_data_submit_name, windows_name)
        res = self.find(self._location_ready_online_error_res).text
        return res






    def goto_channel_in_app_promos(self):
        pass
    def goto_channel_push_notifications(self):
        pass
    def goto_channel_sms_messages(self):
        pass
    def goto_channel_webhook(self):
        pass
    def goto_channel_we_chat_reach(self):
        pass
