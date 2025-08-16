import allure
from config_local import (
    base_url_ui, film_name, actor_name)
from UI_test.pages.main_page import MainPage
from UI_test.pages.search_results_page import SearchResultsPage


@allure.feature("Поиск фильмов")
@allure.story("Поиск фильма по названию")
def test_search_film(browser):
    main_page = MainPage(browser)
    main_page.open(base_url_ui)
    main_page.search(film_name)

    results_page = SearchResultsPage(browser)
    results = results_page.find_film(film_name)
    assert results, f"Фильм '{film_name}' не найден."


@allure.feature("Поиск фильмов")
@allure.story("Поиск фильмов по имени актёра")
def test_search_films_by_actor(browser):
    main_page = MainPage(browser)
    main_page.open(base_url_ui)
    main_page.search(actor_name)

    results_page = SearchResultsPage(browser)
    results = results_page.find_actor(actor_name)
    assert results, f"Фильмы с актёром '{actor_name}' не найдены."
