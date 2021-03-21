# -*- coding:utf-8 -*- #
# @time 2021-03-10 18:01
# author:pengda
from log import logging
import allure
from selenium.webdriver.common.by import By

# logging.basicConfig(level=logging.INFO)
_error_num = 0


# 查找元素方法的装饰器
def handle_black(func):

    def wrapper(*args, **kwargs):
        from basepage.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@text='以后在说']")
        ]
        _max_num = 3
        global _error_num
        # 获取实例化的对象
        instance: BasePage = args[0]
        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0

            # 隐式等待回复原来的等待，
            instance._driver.implicitly_wait(5)
            return element

        except Exception as e:
            # instance.screen_shot(inspect.stack()[2].function)
            logging.error("element not found, handle black list")
            # 重置隐式等待时间
            instance._driver.implicitly_wait(1)

            # 判断异常处理次数
            if _error_num > _max_num:
                instance.screen_shot('tmp.png')
                with open("tmp.png", "rb") as f:
                    content = f.read()

                # 将截图插入allure报告中
                allure.attach(content, attachment_type=allure.attachment_type.PNG)
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance._finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return wrapper(*args, **kwargs)
            return wrapper(*args, **kwargs)
            # raise e

    return wrapper
