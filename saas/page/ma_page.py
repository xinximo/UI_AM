#!/usr/bin/python3
# @Time    : 2021/3/15 2:48 下午
# @Author  : WangXin
from selenium.webdriver.common.by import By

from saas.base_page import SaasBasePage
from saas.page.ma_activity_page import MaActivityPage
from saas.page.workflow_page import WorkFlowPage


class MaPage(SaasBasePage):
    _location_marketing_activity = (By.CSS_SELECTOR, 'a[href="/projects/nxog09md/marketing-automation/plans/all"]')

    def goto_marketing_activity(self):
        self.find_click(self._location_marketing_activity)
        return MaActivityPage(self.driver)

    def goto_workflow(self):
        return WorkFlowPage(self.driver)
