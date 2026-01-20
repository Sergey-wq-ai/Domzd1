from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")
    
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """Заполнить информацию о доставке"""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
    
    def click_continue(self):
        """Нажать кнопку Continue"""
        self.driver.find_element(*self.continue_button).click()
    
    def click_cancel(self):
        """Нажать кнопку Cancel"""
        self.driver.find_element(*self.cancel_button).click()
    
    def click_finish(self):
        """Нажать кнопку Finish"""
        self.driver.find_element(*self.finish_button).click()
    
    def get_total_amount(self):
        """Получить итоговую сумму"""
        total_text = self.driver.find_element(*self.total_label).text
        # Извлекаем число из строки "Total: $58.29"
        return total_text.replace("Total: $", "")
    
    def get_subtotal_amount(self):
        """Получить промежуточную сумму"""
        subtotal_element = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        subtotal_text = subtotal_element.text
        return subtotal_text.replace("Item total: $", "")
    
    def get_tax_amount(self):
        """Получить сумму налога"""
        tax_element = self.driver.find_element(By.CLASS_NAME, "summary_tax_label")
        tax_text = tax_element.text
        return tax_text.replace("Tax: $", "")
    
    def is_order_complete(self):
        """Проверить, завершен ли заказ"""
        try:
            complete_text = self.driver.find_element(*self.complete_header).text
            return "THANK YOU FOR YOUR ORDER" in complete_text
        except:
            return False