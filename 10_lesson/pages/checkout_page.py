from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object для страницы оформления заказа Sauce Demo."""
    
    def __init__(self, driver):
        """
        Инициализирует CheckoutPage.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы формы
        self.FIRST_NAME_INPUT = (By.ID, "first-name")
        self.LAST_NAME_INPUT = (By.ID, "last-name")
        self.POSTAL_CODE_INPUT = (By.ID, "postal-code")
        
        # Локаторы кнопок
        self.CONTINUE_BUTTON = (By.ID, "continue")
        self.CANCEL_BUTTON = (By.ID, "cancel")
        self.FINISH_BUTTON = (By.ID, "finish")
        
        # Локаторы итоговой информации
        self.TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
        self.SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
        self.TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
        
        # Локаторы подтверждения заказа
        self.COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
        self.COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    
    @allure.step("Заполнить информацию о доставке: {first_name} {last_name}, индекс: {postal_code}")
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """
        Заполняет информацию о доставке.
        
        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
            
        Returns:
            None
        """
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
    
    @allure.step("Нажать кнопку Continue")
    def click_continue(self):
        """
        Нажимает кнопку Continue для перехода к итогам заказа.
        
        Returns:
            None
        """
        self.click_element(self.CONTINUE_BUTTON)
    
    @allure.step("Нажать кнопку Cancel")
    def click_cancel(self):
        """
        Нажимает кнопку Cancel для отмены оформления заказа.
        
        Returns:
            None
        """
        self.click_element(self.CANCEL_BUTTON)
    
    @allure.step("Нажать кнопку Finish")
    def click_finish(self):
        """
        Нажимает кнопку Finish для завершения заказа.
        
        Returns:
            None
        """
        self.click_element(self.FINISH_BUTTON)
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self):
        """
        Получает итоговую сумму заказа.
        
        Returns:
            str: Итоговая сумма (например: "58.29")
        """
        try:
            total_text = self.find_element(self.TOTAL_LABEL).text
            return total_text.replace("Total: $", "")
        except:
            return "0.00"
    
    @allure.step("Получить промежуточную сумму товаров")
    def get_subtotal_amount(self):
        """
        Получает промежуточную сумму товаров.
        
        Returns:
            str: Сумма товаров (например: "49.99")
        """
        try:
            subtotal_element = self.find_element(self.SUBTOTAL_LABEL)
            subtotal_text = subtotal_element.text
            return subtotal_text.replace("Item total: $", "")
        except:
            return "0.00"
    
    @allure.step("Получить сумму налога")
    def get_tax_amount(self):
        """
        Получает сумму налога.
        
        Returns:
            str: Сумма налога (например: "8.30")
        """
        try:
            tax_element = self.find_element(self.TAX_LABEL)
            tax_text = tax_element.text
            return tax_text.replace("Tax: $", "")
        except:
            return "0.00"
    
    @allure.step("Проверить, что заказ завершен")
    def is_order_complete(self):
        """
        Проверяет, успешно ли завершен заказ.
        
        Returns:
            bool: True если заказ завершен, иначе False
        """
        try:
            complete_text = self.find_element(self.COMPLETE_HEADER).text
            return "THANK YOU FOR YOUR ORDER" in complete_text
        except:
            return False
    
    @allure.step("Получить текст подтверждения заказа")
    def get_completion_text(self):
        """
        Получает текст подтверждения заказа.
        
        Returns:
            str: Текст подтверждения заказа
        """
        try:
            return self.find_element(self.COMPLETE_TEXT).text
        except:
            return ""
    
    @allure.step("Проверить, что страница оформления заказа загружена")
    def is_checkout_page_loaded(self):
        """
        Проверяет, загружена ли страница оформления заказа.
        
        Returns:
            bool: True если страница загружена, иначе False
        """
        try:
            return "checkout" in self.driver.current_url
        except:
            return False
    
    @allure.step("Проверить, что заказ создан успешно")
    def verify_order_success(self):
        """
        Проверяет успешность создания заказа.
        
        Returns:
            bool: True если заказ создан успешно
        """
        return self.is_order_complete() and "checkout-complete.html" in self.driver.current_url