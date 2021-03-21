#!/usr/bin/python3
# @Time    : 2021/3/15 3:44 下午
# @Author  : WangXin
import configparser
import os

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SaasBasePage:
    FIND = 'find'
    ACTION = 'action'
    CONTENT = 'content'
    FIND_CLICK = 'find_click'
    SEND = 'send_keys'

    def __init__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver

        # if base_driver is None:
        #     self.driver = webdriver.Chrome()
        #     self.driver.maximize_window()
        #     self.driver.get("https://release-www.growingio.cn")
        #     # self._test_login()
        # else:
        #     self.driver = base_driver
        # self.driver.implicitly_wait(10)

        config = self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        try:
            browser = os.environ["browser"]
        except KeyError:
            browser = None
            print('没有配置环境变量 browser, 按照默认有界面方式运行自动化测试')

        chrome_options = Options()
        if browser is not None and browser.lower() == 'no_gui':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                           options=chrome_options)
        elif browser is not None and browser.lower() == 'chrome_remote':
            docker_remote = config.get('driver', 'chrome_remote')
            print(f'使用远程方式运行, remote url:{docker_remote}')
            self.driver = webdriver.Remote(command_executor=docker_remote,
                                           desired_capabilities=DesiredCapabilities.CHROME)

        elif browser is not None and browser.lower() == 'firefox_remote':
            docker_firefox_remote = config.get('driver', 'firefox_remote')
            print(f'使用远程方式运行, remote url:{docker_firefox_remote}')
            self.driver = webdriver.Remote(command_executor=docker_firefox_remote,
                                           desired_capabilities=DesiredCapabilities.FIREFOX)
        else:
            print('使用有界面Chrome浏览器运行')
            self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                           options=chrome_options)
        # self.driver.maximize_window()
        self.driver.get("https://release-www.growingio.cn")
        self.driver.implicitly_wait(10)

    # def _test_login(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = '127.0.0.1:9222'
    #     driver = webdriver.Chrome(options=opt)
    #     driver.implicitly_wait(5)
    #     driver.get("https://release-www.growingio.cn/platform")
    #     cookie = driver.get_cookies()
    #     with open("data/saas_cookie.yml", "w", encoding="UTF-8") as f:
    #         yaml.dump(cookie, f)
    #     with open("data/saas_cookie.yml", "r", encoding="UTF-8") as f:
    #         yaml_data = yaml.safe_load(f)
    #     for cookie in yaml_data:
    #         self.driver.add_cookie(cookie)
    #     self.driver.get("https://release-www.growingio.cn/platform")

    def find(self, locator, value=None):
        if value is None:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(by=locator, value=value)

    def finds(self, locator, value=None):
        if value is None:
            return self.driver.find_elements(*locator)
        else:
            return self.driver.find_elements(by=locator, value=value)

    def find_click(self, locator, value=None):
        self.find(locator, value=value).click()

    def send_keys(self, locator, keys, value: str = None, advance_clear=False):
        """

        :param locator: 定位方式，可以是tuple或者str
                        eg：(By.CSS_SELECTOR, "#id_content")或者By.CSS_SELECTOR
        :param keys: 输入框内输入的内容
        :param value: 页面元素的定位内容，可以为空
        :param advance_clear: 标示符，输入内容之前是否要先清空，默认不清空
        :return:
        """
        if advance_clear:
            self.find(locator, value).clear()
            self.find(locator, value).send_keys(keys)
        else:
            self.find(locator, value).send_keys(keys)

    def send_keys_clear(self, locator, value=None):
        """
        清空非text的可输入框,例如input类型里面的value默认值
        """
        _key = self.find(locator)
        _key.send_keys(Keys.COMMAND + 'a')
        _key.send_keys(Keys.DELETE)
        _key.send_keys(value)

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(locator))

    def quit_browser(self):
        self.driver.quit()

    def load(self, yaml_path):
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f)
        for step in data:
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            content = step.get(self.CONTENT)
            if action == self.FIND_CLICK:
                self.find_click(By.XPATH, xpath_expr)
            elif action == self.SEND:
                self.send_keys(By.XPATH, xpath_expr, content)

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        return config
