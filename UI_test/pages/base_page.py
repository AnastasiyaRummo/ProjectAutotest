import allure
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Найти элемент: {by}={value}")
    def find(self, by, value):
        return self.browser.find_element(by, value)

    @allure.step("Найти все элементы: {by}={value}")
    def find_all(self, by, value):
        return self.browser.find_elements(by, value)

    @allure.step("Получить текст заголовка страницы")
    def get_header_text(self):
        return self.find(By.TAG_NAME, "h1").text
