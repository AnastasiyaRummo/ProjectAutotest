import allure
from selenium.webdriver.common.by import By
from UI_test.pages.base_page import BasePage


class ArticlesPage(BasePage):
    first_article = (
        By.CSS_SELECTOR,
        "div.styles_scrollBar__gXL4U div[role='list'] > *:first-child")
    article_title = (By.TAG_NAME, "h1")

    @allure.step("Открыть первую статью")
    def open_first_article(self):
        self.find(*self.first_article).click()

    @allure.step("Получить заголовок статьи")
    def get_title(self):
        return self.find(*self.article_title).text
