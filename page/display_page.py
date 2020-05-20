from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    display_button = By.XPATH, "//*[contains(@text, '显示')]"

    search_button = By.ID, "com.android.settings:id/search"

    text_input = By.ID, "android:id/search_src_text"

    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # self.driver = driver
        # self.click_display()

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '显示')]").click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text, '显示')]").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element(By.ID, "com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.driver.find_element(By.ID, "android:id/search_src_text").send_key(text)
        # self.find_element(self.text_input).send_key(text)
        self.input(self.text_input, "what")

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.driver.find_element(By.CLASS_NAME, "android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)

    def find_element(self, loc):
        self.find_element(loc[0], loc[1])
