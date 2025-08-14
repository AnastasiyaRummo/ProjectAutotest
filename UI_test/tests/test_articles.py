import allure
from selenium.webdriver.support.ui import WebDriverWait
from ProjectAutotest.UI_test.config_local import base_url
from ProjectAutotest.UI_test.pages.base_page import BasePage
from ProjectAutotest.UI_test.pages.articles_page import ArticlesPage


@allure.feature("Просмотр статьи")
@allure.story("Открыть статью и проверить заголовок")
def test_view_article(browser):
    base_page = BasePage(browser)
    base_page.open(base_url)

    articles_page = ArticlesPage(browser)
    WebDriverWait(browser, 20)
    articles_page.open_first_article()

    title = articles_page.get_title()
    assert title, "Заголовок статьи пустой."
