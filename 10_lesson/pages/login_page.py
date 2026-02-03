from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы авторизации Sauce Demo."""
    
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        """
        Инициализирует LoginPage.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
    
    @allure.step("Открыть страницу авторизации")
    def open(self, url=None):
        """
        Открывает страницу авторизации.
        
        Args:
            url: URL страницы (если None, используется дефолтный)
            
        Returns:
            None
        """
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)
    
    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username):
        """
        Вводит имя пользователя.
        
        Args:
            username: Имя пользователя для ввода
            
        Returns:
            None
        """
        self.send_keys(self.USERNAME_INPUT, username)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """
        Вводит пароль.
        
        Args:
            password: Пароль для ввода
            
        Returns:
            None
        """
        self.send_keys(self.PASSWORD_INPUT, password)
    
    @allure.step("Нажать кнопку Login")
    def click_login(self):
        """
        Нажимает кнопку входа.
        
        Returns:
            None
        """
        self.click_element(self.LOGIN_BUTTON)
    
    @allure.step("Выполнить авторизацию с логином: {username}")
    def login(self, username, password):
        """
        Выполняет полную авторизацию.
        
        Args:
            username: Имя пользователя
            password: Пароль
            
        Returns:
            None
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        """
        Получает текст сообщения об ошибке.
        
        Returns:
            str: Текст ошибки или пустая строка
        """
        try:
            return self.find_element(self.ERROR_MESSAGE, timeout=2).text
        except:
            return ""