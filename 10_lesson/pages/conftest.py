import pytest
import allure
from selenium import webdriver


def pytest_configure(config):
    """Конфигурация pytest для Allure."""
    config.option.allure_report_dir = "./allure-results"


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания WebDriver.
    
    Yields:
        WebDriver: Экземпляр WebDriver
    """
    with allure.step("Инициализация WebDriver"):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
    
    yield driver
    
    with allure.step("Закрытие WebDriver"):
        driver.quit()


@pytest.fixture
def login_page(driver):
    """Фикстура для LoginPage."""
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    """Фикстура для InventoryPage."""
    from pages.inventory_page import InventoryPage
    return InventoryPage(driver)