import allure
from selenium.webdriver.common.by import By
from config_local import (
    base_url_ui, film_name, film_year, genre)
from UI_test.pages.base_page import BasePage
from UI_test.pages.advanced_search_page import (
    AdvancedSearchPage)


@allure.title("Проверка поиска фильма по названию, году и жанру")
@allure.description(
    "Тест выполняет расширенный поиск фильма с использованием фильтров: "
    "название, год выпуска и жанр. Проверяется наличие результатов и "
    "наличие нужного фильма в списке.")
@allure.feature("Расширенный поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_advanced_search(browser):
    base_page = BasePage(browser)
    with allure.step("Открыть главную страницу"):
        base_page.open(base_url_ui)

    with allure.step("Переход в расширенный поиск"):
        advanced_search = browser.find_element(
            By.CSS_SELECTOR, "a[aria-label='Расширенный поиск']")
        advanced_search.click()

    advanced_page = AdvancedSearchPage(browser)
    with allure.step(f"Установить название фильма: {film_name}"):
        advanced_page.set_name(film_name)
    with allure.step(f"Установить год выпуска: {film_year}"):
        advanced_page.set_year(film_year)
    with allure.step(f"Выбрать жанр: {genre}"):
        advanced_page.select_genre(genre)
    with allure.step("Выполнить поиск"):
        advanced_page.submit_search()

    with allure.step("Проверить, что результаты поиска не пустые"):
        results = advanced_page.get_results()
        assert results, "Результаты поиска пустые."

    with allure.step(f"Проверить, что фильм '{film_name}' найден в результатах"
                     ):
        found = any(film_name.lower() in r.text.lower() for r in results)
        assert found, f"Фильм '{film_name}' не найден в результатах."
