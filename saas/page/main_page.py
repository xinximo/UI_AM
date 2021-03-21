#!/usr/bin/python3
# @Time    : 2021/3/15 2:07 下午
# @Author  : WangXin
from selenium.webdriver.common.by import By

from saas.base_page import SaasBasePage
from saas.page.ma_page import MaPage


class MainPage(SaasBasePage):
    _location_marketing_auto = (By.CSS_SELECTOR, 'a[href="/projects/nxog09md/marketing-automation/"]')
    _location_personal_data = (By.XPATH, '//span[@class="ant-avatar-string"]')
    _location_group_data = (By.XPATH, '//div[@class="ant-select-selection-selected-value"]/span')
    _location_main = (By.CSS_SELECTOR, ".platform-app-logo-wrapper")

    def goto_product_analytics(self):
        # 跳转产品分析页面
        pass

    def goto_marketing_auto(self):
        # 跳转智能运营页面
        self.wait_click(self._location_marketing_auto)
        self.find(self._location_marketing_auto).click()
        return MaPage(self.driver)

    def goto_acquisition_analytics(self):
        # 跳转获客分析页面
        pass

    def goto_user_warehouse(self):
        # 跳转用户库页面
        pass

    def goto_data_center(self):
        # 跳转数据中心页面
        pass

    def goto_project_management(self):
        # 跳转项目管理页面
        pass

    def get_index_assert_text(self):
        self.wait_click(self._location_group_data)
        return self.find(self._location_group_data).text
