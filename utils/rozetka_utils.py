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
        self.search_item_grid = (By.XPATH, "//li[contains(@class, 'catalog-grid')]//a[contains(@title, '%s')]")
        self.main_item_title = (By.XPATH, "//h1[@class='product__title']")

    def open_rozetka_page(self):
        self.custom_driver.open_url(self.url)
    def search_item(self, search_text):
        self.custom_driver.input_text(self.search_input, search_text)
        self.custom_driver.click_web_element(self.search_icon)
        current_title = self.custom_driver.wait_web_element(self.search_title).text
        current_title = current_title.replace('«', '').replace('»', '')
        assert search_text == current_title, f"Actual title: {current_title} doesn't match with expected: {search_text}"

    def select_item_from_grid(self, text: str):
        selector = self.custom_driver.format_selector(self.search_item_grid, text)
        item_title_search = self.custom_driver.get_attribute_text(selector)
        clickable_element = f"{selector[1]}//.."
        selector = list(selector)
        selector[1] = clickable_element
        selector = tuple(selector)
        self.custom_driver.click_web_element(selector)
        title = self.custom_driver.wait_web_element(self.main_item_title).text
        assert item_title_search == title, f"Actual title: {title} doesn't match with expected: {item_title_search}"



