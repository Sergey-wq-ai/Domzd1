from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_button = (By.ID, "continue-shopping")
    
    def click_checkout(self):
        """Нажать кнопку Checkout"""
        self.driver.find_element(*self.checkout_button).click()
    
    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        return len(self.driver.find_elements(*self.cart_items))
    
    def get_item_names(self):
        """Получить названия всех товаров в корзине"""
        items = self.driver.find_elements(*self.cart_items)
        item_names = []
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            item_names.append(name_element.text)
        return item_names
    
    def continue_shopping(self):
        """Вернуться к покупкам"""
        self.driver.find_element(*self.continue_shopping_button).click()