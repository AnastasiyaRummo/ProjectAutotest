import sys
import os
import pytest
import allure
import config_local as cfg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# для API тестов:
@pytest.fixture(scope="session")
def base_url():
    return cfg.base_url_api


@pytest.fixture(scope="session")
def headers():
    return cfg.headers


@pytest.fixture(scope="session")
def film_id():
    return cfg.film_id


@pytest.fixture(scope="session")
def serial_data():
    return {
        "id": cfg.serial_id,
        "season": cfg.season_number,
        "episode": cfg.episode_number
    }


# для UI тестов
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
