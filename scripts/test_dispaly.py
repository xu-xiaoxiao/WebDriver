import os, sys

import allure
import pytest
import allure_pytest

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDispaly:
    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("测试搜索框")
    def test_search(self):
        allure.attach("输入内容", "内容的描述")
        # 点击显示
        self.display_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_text("hello")
        # 点击返回
        self.display_page.click_back()
