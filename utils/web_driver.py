from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomWebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://stvol.ua/"
        self.timeOut = 30

        self.search_icon = "//button[@data-toggle-trigger='search']"
        self.search_input = "//input[@id='search']"
        self.pistol_1st = "//div[@class='product-card__image-wrapper']//img[contains(@alt, 'пістолет')][1]"




    def open_url(self):
        self.driver.get(self.url)


CustomWebDriver().open_url()