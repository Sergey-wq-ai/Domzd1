from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        
        # Локаторы для кнопок добавления товаров
        self.add_to_cart_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
            "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
            "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
            "Test.allTheThings() T-Shirt (Red)": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        }
    
    def add_item_to_cart(self, item_name):
        """Добавить товар в корзину по названию"""
        locator = self.add_to_cart_buttons.get(item_name)
        if locator:
            self.driver.find_element(*locator).click()
            return True
        return False
    
    def add_multiple_items_to_cart(self, items_list):
        """Добавить несколько товаров в корзину"""
        for item in items_list:
            self.add_item_to_cart(item)
    
    def go_to_cart(self):
        """Перейти в корзину"""
        self.driver.find_element(*self.cart_button).click()
    
    def get_cart_count(self):
        """Получить количество товаров в корзине"""
        cart_element = self.driver.find_element(*self.cart_button)
        text = cart_element.text
        return int(text) if text else 0