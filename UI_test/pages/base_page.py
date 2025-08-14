from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find(self, by, value):
        return self.browser.find_element(by, value)

    def find_all(self, by, value):
        return self.browser.find_elements(by, value)

    def get_header_text(self):
        return self.find(By.TAG_NAME, "h1").text
