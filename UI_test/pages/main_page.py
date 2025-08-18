import allure
from selenium.webdriver.common.by import By
from UI_test.pages.base_page import BasePage


class MainPage(BasePage):
    search_input = (By.CSS_SELECTOR, "input[placeholder*='Фильмы']")
    advanced_search = (By.CSS_SELECTOR, "a[aria-label='Расширенный поиск']")

    @allure.step("Выполнить поиск: {text}")
    def search(self, text):
        search_input = self.find(*self.search_input)
        search_input.clear()
        search_input.send_keys(text)
        search_input.submit()

    @allure.step("Перейти в расширенный поиск")
    def go_to_advanced_search(self):
        self.find(*self.advanced_search).click()
