from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


class CustomWebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.timeout = 30

        self.search_icon = (By.XPATH, "//button[contains(@class, 'submit ng-star-inserted')]")
        self.search_input = (By.XPATH, "//input[@name='search']")
        self.pistol_1st = "//div[@class='product-card__image-wrapper']//img[contains(@alt, 'пістолет')][1]"
        self.language_selector = (By.XPATH, "//span[@class='button__text' and contains (text(),'UA')]")
        self.search_title = (By.XPATH, "//h1[@class='catalog-heading ng-star-inserted']")


    def open_url(self, url):
        self.driver.get(url)

    def wait_web_element(self, element):
        wait_lib = WebDriverWait(self.driver, self.timeout)
        web_element = wait_lib.until(EC.presence_of_element_located((element[0], element[1])))
        return web_element

    def click_web_element(self, element):
        elem = self.wait_web_element(element)
        elem.click()

    def input_text(self, element, text):
        elem = self.wait_web_element(element)
        elem.send_keys(text)

