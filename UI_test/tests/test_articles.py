import allure
from selenium.webdriver.support.ui import WebDriverWait
from config_local import base_url_ui
from UI_test.pages.base_page import BasePage
from UI_test.pages.articles_page import ArticlesPage


@allure.title("Проверка открытия статьи и отображения заголовка")
@allure.description(
    "Тест открывает главную страницу, переходит в раздел статей, "
    "открывает первую статью и проверяет наличие заголовка.")
@allure.feature("Просмотр статьи")
@allure.severity(allure.severity_level.NORMAL)
def test_view_article(browser):
    base_page = BasePage(browser)

    with allure.step("Открыть главную страницу"):
        base_page.open(base_url_ui)
    with allure.step("Перейти на страницу статей"):
        articles_page = ArticlesPage(browser)
    with allure.step("Ожидание загрузки страницы статей"):
        WebDriverWait(browser, 20)
    with allure.step("Открыть первую статью"):
        articles_page.open_first_article()
    with allure.step("Проверить, что заголовок статьи не пустой"):
        title = articles_page.get_title()
        assert title, "Заголовок статьи пустой."
