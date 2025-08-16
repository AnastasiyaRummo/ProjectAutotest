import allure
from selenium.webdriver.support.ui import WebDriverWait
from config_local import (
    base_url_ui, film_name, actor_name)
from UI_test.pages.main_page import MainPage
from UI_test.pages.search_results_page import SearchResultsPage
from UI_test.pages.film_and_actor_page import (FilmPage,
                                               ActorPage)


@allure.feature("Просмотр фильма")
@allure.story("Открыть страницу фильма и проверить заголовок")
def test_view_film_page(browser):
    main_page = MainPage(browser)
    main_page.open(base_url_ui)
    main_page.search(film_name)

    results_page = SearchResultsPage(browser)
    films = results_page.find_film(film_name)
    assert films, f"Фильм '{film_name}' не найден в результатах"
    WebDriverWait(browser, 20)
    films[0].click()

    film_page = FilmPage(browser)
    title = film_page.get_header_text()
    assert film_name.lower() in title.lower()


@allure.feature("Просмотр страницы актёра")
@allure.story("Открыть страницу актёра и проверить заголовок")
def test_view_actor_page(browser):
    main_page = MainPage(browser)
    main_page.open(base_url_ui)
    main_page.search(actor_name)

    results_page = SearchResultsPage(browser)
    actors = results_page.find_actor(actor_name)
    assert actors, f"Актёр '{actor_name}' не найден"
    WebDriverWait(browser, 20)
    actors[0].click()

    actor_page = ActorPage(browser)
    name = actor_page.get_header_text()
    assert actor_name.lower() in name.lower()
