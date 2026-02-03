
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех Page Object.
    
    Args:
        driver: WebDriver instance
    """
    
    def __init__(self, driver):
        """
        Инициализирует BasePage.
        
        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator, timeout=10):
        """
        Находит элемент с ожиданием.
        
        Args:
            locator: Кортеж (By, locator_string)
            timeout: Время ожидания в секундах
            
        Returns:
            WebElement: Найденный элемент
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout=10):
        """
        Находит все элементы с ожиданием.
        
        Args:
            locator: Кортеж (By, locator_string)
            timeout: Время ожидания в секундах
            
        Returns:
            list[WebElement]: Список найденных элементов
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        """
        Кликает на элемент.
        
        Args:
            locator: Кортеж (By, locator_string)
            
        Returns:
            None
        """
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        """
        Вводит текст в поле.
        
        Args:
            locator: Кортеж (By, locator_string)
            text: Текст для ввода
            
        Returns:
            None
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)