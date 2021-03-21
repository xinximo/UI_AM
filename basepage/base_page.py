# -*- coding:utf-8 -*- #
# @time 2021-03-10 11:51
# author:pengda
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

# from selenium.webdriver import Remote  # selelnium-grid分布式打开浏览器使用的类
from selenium.webdriver.support.wait import WebDriverWait

from util.util import handle_black


class BasePage:
    _parmas = {}

    def __init__(self, driver: webdriver = None):

        if not driver:

            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(10)
        else:
            self._driver = driver

    # 打开被测网站
    def open_url(self, target_url):
        from saas.page.login_page import LoginPage
        self._driver.get(target_url)
        return LoginPage(self._driver)

    # 获取元素文本
    def get_element_text(self, locator, value: str = None):
        element = self._find(locator, value)
        return element.text

    # 定位单一元素
    @handle_black
    def _find(self, locator, value: str = None)-> WebElement:
        # sleep(1)
        if isinstance(locator, tuple):
            # 显示等待查找元素
            # element = WebDriverWait(self._driver, 10).until(lambda driver: driver.find_element(*locator))
            # 显示等待+条件判断，等到元素加载到dom中且可见
            element = WebDriverWait(self._driver, 10).until(ec.visibility_of_element_located(locator))
        else:
            element = self._driver.find_element(locator, value)
        return element

    # 定位多个元素
    def _finds(self, locator, value: str = None) -> list:
        if isinstance(locator, tuple):
            return self._driver.find_elements(*locator)
        else:
            return self._driver.find_elements(locator, value)

    # 通用点击操作
    def click(self, locator, value: str = None):
        self._find(locator, value).click()

    # 通用输入操作
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
            self._find(locator, value).clear()
            self._find(locator, value).send_keys(keys)
        else:
            self._find(locator, value).send_keys(keys)

    # 获取元素文本
    def get_text(self, locator, value: str = None)-> str:
        return self._find(locator, value).text

    # 鼠标移动悬停事件
    def move_mouse_stop(self, locator):
        ActionChains(self._driver).move_to_element(self._find(locator)).perform()

    # 切换窗口句柄
    def switch_to_window_by_title(self, window_title):
        """window_title: 窗口title"""
        all_handles = self._driver.window_handles
        for window_handle in all_handles:
            self.switch_to_target_window(window_handle)
            if self._driver.title == window_title:
                return
        raise Exception("不存在目标窗口，切换窗口句柄失败！")

    # 切换到某个窗口
    def switch_to_target_window(self, window_handle):
        """window_handle：窗口句柄"""
        self._driver.switch_to_window(window_handle)

    # 获取当前窗口句柄
    def get_current_window_handle(self):
        return self._driver.current_window_handle

    # 截屏
    def screen_shot(self, filename):
        self._driver.get_screenshot_as_file(filename)

    # 关闭浏览器
    def close_browser(self):
        self._driver.quit()
