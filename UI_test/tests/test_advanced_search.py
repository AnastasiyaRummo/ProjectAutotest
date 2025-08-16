import allure
from selenium.webdriver.common.by import By
from config_local import (
    base_url_ui, film_name, film_year, genre)
from UI_test.pages.base_page import BasePage
from UI_test.pages.advanced_search_page import (
    AdvancedSearchPage)


@allure.feature("Расширенный поиск")
@allure.story("Поиск фильма с фильтрами: название, год, жанр")
def test_advanced_search(browser):
    base_page = BasePage(browser)
    base_page.open(base_url_ui)

    # Переход в расширенный поиск
    advanced_search = browser.find_element(By.CSS_SELECTOR,
                                           "a[aria-label='Расширенный поиск']")
    advanced_search.click()

    advanced_page = AdvancedSearchPage(browser)
    advanced_page.set_name(film_name)
    advanced_page.set_year(film_year)
    advanced_page.select_genre(genre)
    advanced_page.submit_search()

    results = advanced_page.get_results()
    assert results, "Результаты поиска пустые."

    found = any(film_name.lower() in r.text.lower() for r in results)
    assert found, f"Фильм '{film_name}' не найден в результатах."
