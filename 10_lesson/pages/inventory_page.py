from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class InventoryPage(BasePage):
    """Page Object для страницы товаров Sauce Demo."""
    
    def __init__(self, driver):
        """
        Инициализирует InventoryPage.
        
        Args:
            driver: Экземпляр WebDriver
        """
        super().__init__(driver)
        
        # Локаторы
        self.CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
        self.CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
        
        # Локаторы для кнопок добавления товаров
        self.ADD_TO_CART_BUTTONS = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
            "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
            "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
            "Test.allTheThings() T-Shirt (Red)": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        }
    
    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name):
        """
        Добавляет товар в корзину по названию.
        
        Args:
            item_name: Название товара для добавления
            
        Returns:
            bool: True если товар найден и добавлен, иначе False
        """
        locator = self.ADD_TO_CART_BUTTONS.get(item_name)
        if locator:
            self.click_element(locator)
            return True
        return False
    
    @allure.step("Добавить несколько товаров в корзину: {items_list}")
    def add_multiple_items_to_cart(self, items_list):
        """
        Добавляет несколько товаров в корзину.
        
        Args:
            items_list: Список названий товаров для добавления
            
        Returns:
            None
        """
        for item in items_list:
            self.add_item_to_cart(item)
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Переходит в корзину покупок.
        
        Returns:
            None
        """
        self.click_element(self.CART_BUTTON)
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self):
        """
        Получает количество товаров в корзине.
        
        Returns:
            int: Количество товаров в корзине (0 если корзина пуста)
        """
        try:
            cart_element = self.find_element(self.CART_BADGE, timeout=2)
            text = cart_element.text
            return int(text) if text else 0
        except:
            return 0
    
    @allure.step("Проверить, что страница товаров загружена")
    def is_page_loaded(self):
        """
        Проверяет, загружена ли страница товаров.
        
        Returns:
            bool: True если страница загружена, иначе False
        """
        try:
            return "inventory.html" in self.driver.current_url
        except:
            return False
    
    @allure.step("Получить названия всех товаров на странице")
    def get_all_item_names(self):
        """
        Получает названия всех товаров на странице.
        
        Returns:
            list[str]: Список названий товаров
        """
        item_names = []
        try:
            items = self.find_elements((By.CLASS_NAME, "inventory_item_name"))
            item_names = [item.text for item in items]
        except:
            pass
        return item_names
    
    @allure.step("Получить цены всех товаров на странице")
    def get_all_item_prices(self):
        """
        Получает цены всех товаров на странице.
        
        Returns:
            list[str]: Список цен товаров
        """
        item_prices = []
        try:
            items = self.find_elements((By.CLASS_NAME, "inventory_item_price"))
            item_prices = [item.text for item in items]
        except:
            pass
        return item_prices