from selenium.webdriver.common.by import By
import re
from utils.web_driver import CustomWebDriver
class RozetkaUtils:
    def __init__(self):
        self.url = "https://rozetka.com.ua/ua/"
        self.custom_driver = CustomWebDriver()

        self.search_icon = (By.XPATH, "//button[contains(@class, 'submit ng-star-inserted')]")
        self.search_input = (By.XPATH, "//input[@name='search']")
        self.search_title = (By.XPATH, "//h1[@class='catalog-heading ng-star-inserted']")

    def open_rozetka_page(self):
        self.custom_driver.open_url(self.url)
    def search_item(self, search_text):
        self.custom_driver.input_text(self.search_input, search_text)
        self.custom_driver.click_web_element(self.search_icon)
        current_title = self.custom_driver.wait_web_element(self.search_title).text
        current_title = current_title.replace('«', '').replace('»', '')
        assert search_text == current_title, f"Actual title: {current_title} doesn't match with expected: {search_text}"