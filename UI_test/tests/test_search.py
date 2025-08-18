import allure
from config_local import (
    base_url_ui, film_name, actor_name)
from UI_test.pages.main_page import MainPage
from UI_test.pages.search_results_page import SearchResultsPage


@allure.title("Проверка поиска фильма по названию")
@allure.description(
    "Тест открывает главную страницу, выполняет поиск фильма по названию "
    "и проверяет, что найден хотя бы один результат.")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_film(browser):
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу"):
        main_page.open(base_url_ui)
    with allure.step(f"Выполнить поиск фильма: {film_name}"):
        main_page.search(film_name)
    with allure.step("Проверить, что фильм найден в результатах"):
        results_page = SearchResultsPage(browser)
        results = results_page.find_film(film_name)
        assert results, f"Фильм '{film_name}' не найден."


@allure.title("Проверка поиска фильмов по имени актёра")
@allure.description(
    "Тест открывает главную страницу, выполняет поиск фильмов по имени актёра "
    "и проверяет, что найдены результаты.")
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_actor(browser):
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу"):
        main_page.open(base_url_ui)
    with allure.step(f"Выполнить поиск фильмов по актёру: {actor_name}"):
        main_page.search(actor_name)
    with allure.step("Проверить, что фильмы с актёром найдены"):
        results_page = SearchResultsPage(browser)
        results = results_page.find_actor(actor_name)
        assert results, f"Фильмы с актёром '{actor_name}' не найдены."
