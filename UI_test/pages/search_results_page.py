import allure
from selenium.webdriver.common.by import By
from UI_test.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    @allure.step("Найти фильм в результатах поиска: {film_name}")
    def find_film(self, film_name):
        xpath = f"//a[contains(text(), '{film_name}')]"
        return self.find_all(By.XPATH, xpath)

    @allure.step("Найти актёра в результатах поиска: {actor_name}")
    def find_actor(self, actor_name):
        xpath = f"//a[contains(text(), '{actor_name}')]"
        return self.find_all(By.XPATH, xpath)
