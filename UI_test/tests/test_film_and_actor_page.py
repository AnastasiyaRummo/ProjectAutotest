import allure
from selenium.webdriver.support.ui import WebDriverWait
from config_local import (
    base_url_ui, film_name, actor_name)
from UI_test.pages.main_page import MainPage
from UI_test.pages.search_results_page import SearchResultsPage
from UI_test.pages.film_and_actor_page import (FilmPage,
                                               ActorPage)


@allure.title("Проверка открытия страницы фильма")
@allure.description(
    "Тест открывает главную страницу, выполняет поиск по фильму, "
    "открывает страницу фильма и проверяет корректность заголовка.")
@allure.feature("Просмотр фильма")
@allure.severity(allure.severity_level.CRITICAL)
def test_view_film_page(browser):
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу"):
        main_page.open(base_url_ui)
    with allure.step(f"Выполнить поиск фильма: {film_name}"):
        main_page.search(film_name)
    with allure.step("Получить результаты поиска фильмов"):
        results_page = SearchResultsPage(browser)
        films = results_page.find_film(film_name)
        assert films, f"Фильм '{film_name}' не найден в результатах"
    with allure.step("Ожидание загрузки результатов и переход к фильму"):
        WebDriverWait(browser, 20)
        films[0].click()
    with allure.step("Проверить заголовок страницы фильма"):
        film_page = FilmPage(browser)
        title = film_page.get_header_text()
        assert film_name.lower() in title.lower()


@allure.title("Проверка открытия страницы актёра")
@allure.description(
    "Тест открывает главную страницу, выполняет поиск по актёру, "
    "открывает страницу актёра и проверяет корректность заголовка.")
@allure.feature("Просмотр страницы актёра")
@allure.severity(allure.severity_level.NORMAL)
def test_view_actor_page(browser):
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу"):
        main_page.open(base_url_ui)
    with allure.step(f"Выполнить поиск актёра: {actor_name}"):
        main_page.search(actor_name)

    with allure.step("Получить результаты поиска актёров"):
        results_page = SearchResultsPage(browser)
        actors = results_page.find_actor(actor_name)
        assert actors, f"Актёр '{actor_name}' не найден"
    with allure.step("Ожидание загрузки результатов и переход к актёру"):
        WebDriverWait(browser, 20)
        actors[0].click()
    with allure.step("Проверить заголовок страницы актёра"):
        actor_page = ActorPage(browser)
        name = actor_page.get_header_text()
        assert actor_name.lower() in name.lower()
