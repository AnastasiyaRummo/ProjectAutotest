from selenium.webdriver.common.by import By
from UI_test.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def find_film(self, film_name):
        xpath = f"//a[contains(text(), '{film_name}')]"
        return self.find_all(By.XPATH, xpath)

    def find_actor(self, actor_name):
        xpath = f"//a[contains(text(), '{actor_name}')]"
        return self.find_all(By.XPATH, xpath)
