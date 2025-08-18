import allure
from selenium.webdriver.common.by import By
from UI_test.pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    name_input = (By.ID, "find_film")
    year_input = (By.ID, "year")
    genre_select = (By.ID, "m_act[genre]")
    search_button = (By.CSS_SELECTOR, "input.el_18.submit.nice_button")
    result_item = (By.CSS_SELECTOR, "div.element")

    @allure.step("Установить название фильма: {name}")
    def set_name(self, name):
        name_input = self.find(*self.name_input)
        name_input.clear()
        name_input.send_keys(name)

    @allure.step("Установить год выпуска: {year}")
    def set_year(self, year):
        year_input = self.find(*self.year_input)
        year_input.clear()
        year_input.send_keys(year)

    @allure.step("Выбрать жанр: {genre_text}")
    def select_genre(self, genre_text):
        genre_select = self.find(*self.genre_select)
        for option in genre_select.find_elements(
                By.XPATH, "//select[@id='m_act[genre]']//option[@value='3']"):
            if option.text == genre_text:
                option.click()
                break

    @allure.step("Выполнить поиск")
    def submit_search(self):
        self.find(*self.search_button).click()

    @allure.step("Получить результаты поиска")
    def get_results(self):
        return self.find_all(*self.result_item)
