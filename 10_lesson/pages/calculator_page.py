from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class CalculatorPage(BasePage):
    """Page Object для калькулятора с настраиваемой задержкой."""
    
    def __init__(self, driver):
        """
        Инициализирует CalculatorPage.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
        self.RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")
        
        # Локаторы кнопок калькулятора
        self.BUTTONS = {
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '0': (By.XPATH, "//span[text()='0']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='×']"),
            '/': (By.XPATH, "//span[text()='÷']"),
            '=': (By.XPATH, "//span[text()='=']"),
            'C': (By.XPATH, "//span[text()='C']"),
            '(': (By.XPATH, "//span[text()='(']"),
            ')': (By.XPATH, "//span[text()=')']")
        }
    
    @allure.step("Установить задержку вычислений: {delay} секунд")
    def set_delay(self, delay):
        """
        Устанавливает задержку вычислений калькулятора.
        
        Args:
            delay: Задержка в секундах (целое число)
            
        Returns:
            None
        """
        element = self.find_element(self.DELAY_INPUT)
        element.clear()
        element.send_keys(str(delay))
    
    @allure.step("Нажать кнопку калькулятора: '{button}'")
    def click_button(self, button):
        """
        Нажимает кнопку калькулятора.
        
        Args:
            button: Символ кнопки для нажатия (например: '1', '+', '=')
            
        Returns:
            bool: True если кнопка найдена и нажата, иначе False
        """
        locator = self.BUTTONS.get(button)
        if locator:
            self.click_element(locator)
            return True
        return False
    
    @allure.step("Выполнить операцию: {expression}")
    def perform_operation(self, expression):
        """
        Выполняет математическую операцию.
        
        Args:
            expression: Строка с выражением (например: "7+8=")
            
        Returns:
            None
        """
        for char in expression:
            self.click_button(char)
    
    @allure.step("Получить результат вычислений")
    def get_result(self):
        """
        Получает результат вычислений с экрана калькулятора.
        
        Returns:
            str: Текст результата
        """
        return self.find_element(self.RESULT_DISPLAY).text
    
    @allure.step("Очистить калькулятор")
    def clear_calculator(self):
        """
        Очищает калькулятор (нажимает кнопку C).
        
        Returns:
            None
        """
        self.click_button('C')
    
    @allure.step("Вычислить выражение: {expression} с задержкой {delay} секунд")
    def calculate_with_delay(self, expression, delay):
        """
        Выполняет вычисление с заданной задержкой.
        
        Args:
            expression: Математическое выражение
            delay: Задержка в секундах
            
        Returns:
            str: Результат вычисления
        """
        self.set_delay(delay)
        self.perform_operation(expression)
        return self.get_result()
    
    @allure.step("Проверить, что калькулятор загружен")
    def is_calculator_loaded(self):
        """
        Проверяет, загружена ли страница калькулятора.
        
        Returns:
            bool: True если калькулятор загружен, иначе False
        """
        try:
            return "slow-calculator" in self.driver.current_url
        except:
            return False
    
    @allure.step("Проверить, что результат равен {expected_result}")
    def verify_result(self, expected_result):
        """
        Проверяет результат вычислений.
        
        Args:
            expected_result: Ожидаемый результат
            
        Returns:
            bool: True если результат совпадает, иначе False
        """
        actual_result = self.get_result()
        return actual_result == str(expected_result)