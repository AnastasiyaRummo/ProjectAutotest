import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    with allure.step("Открыть и настроить браузер"):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()
