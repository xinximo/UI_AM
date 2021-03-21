# -*- coding:utf-8 -*- #
# @time 2021-03-11 19:37
# author:pengda
from selenium.webdriver.common.by import By

from saas.base_page import SaasBasePage


class ElementDesign(SaasBasePage):

    # 跳转某个导航菜单组件并返回组件的文案
    def choose_navigation_menu(self, num: int):
        """num:从最左面数起，第num个"""
        element_index = [i for i in range(2, 50) if i % 2 == 0]
        if not isinstance(num, int):
            raise Exception('导航菜单组件传参非int类型！')

        self.click(By.XPATH, f'//ul[@role="menu"]/li[{element_index[num]}]')
        return self.get_text(By.XPATH, f'//ul[@role="menu"]/li[{element_index[num]}]')

