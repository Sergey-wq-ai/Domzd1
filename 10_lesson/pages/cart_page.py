from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class CartPage(BasePage):
    """Page Object для страницы корзины Sauce Demo."""
    
    def __init__(self, driver):
        """
        Инициализирует CartPage.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы
        self.CHECKOUT_BUTTON = (By.ID, "checkout")
        self.CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
        self.CART_ITEMS = (By.CLASS_NAME, "cart_item")
        self.REMOVE_BUTTONS = (By.CSS_SELECTOR, "button.cart_button")
    
    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self):
        """
        Нажимает кнопку Checkout для оформления заказа.
        
        Returns:
            None
        """
        self.click_element(self.CHECKOUT_BUTTON)
    
    @allure.step("Нажать кнопку Continue Shopping")
    def continue_shopping(self):
        """
        Нажимает кнопку Continue Shopping для возврата к товарам.
        
        Returns:
            None
        """
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        """
        Получает количество товаров в корзине.
        
        Returns:
            int: Количество товаров в корзине
        """
        items = self.find_elements(self.CART_ITEMS)
        return len(items)
    
    @allure.step("Получить названия всех товаров в корзине")
    def get_item_names(self):
        """
        Получает названия всех товаров в корзине.
        
        Returns:
            list[str]: Список названий товаров
        """
        items = self.find_elements(self.CART_ITEMS)
        item_names = []
        
        for item in items:
            try:
                name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
                item_names.append(name_element.text)
            except:
                pass
        
        return item_names
    
    @allure.step("Получить цены всех товаров в корзине")
    def get_item_prices(self):
        """
        Получает цены всех товаров в корзине.
        
        Returns:
            list[str]: Список цен товаров
        """
        items = self.find_elements(self.CART_ITEMS)
        item_prices = []
        
        for item in items:
            try:
                price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
                item_prices.append(price_element.text)
            except:
                pass
        
        return item_prices
    
    @allure.step("Удалить товар из корзины по индексу: {index}")
    def remove_item_by_index(self, index):
        """
        Удаляет товар из корзины по индексу.
        
        Args:
            index: Индекс товара для удаления (начиная с 0)
            
        Returns:
            bool: True если товар удален, иначе False
        """
        try:
            remove_buttons = self.find_elements(self.REMOVE_BUTTONS)
            if index < len(remove_buttons):
                remove_buttons[index].click()
                return True
        except:
            pass
        return False
    
    @allure.step("Очистить корзину")
    def clear_cart(self):
        """
        Удаляет все товары из корзины.
        
        Returns:
            int: Количество удаленных товаров
        """
        removed_count = 0
        try:
            remove_buttons = self.find_elements(self.REMOVE_BUTTONS)
            for button in remove_buttons:
                button.click()
                removed_count += 1
        except:
            pass
        return removed_count
    
    @allure.step("Проверить, что страница корзины загружена")
    def is_page_loaded(self):
        """
        Проверяет, загружена ли страница корзины.
        
        Returns:
            bool: True если страница загружена, иначе False
        """
        try:
            return "cart.html" in self.driver.current_url
        except:
            return False