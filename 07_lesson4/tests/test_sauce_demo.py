import sys
import os
import time

# Добавляем родительскую папку в путь Python для импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_sauce_demo_checkout():
    """
    Тест для интернет-магазина Sauce Demo
    Проверяет оформление заказа с тремя товарами
    """
    driver = None
    
    try:
        # 1. Создаем драйвер Firefox
        print("1. Запускаем Firefox...")
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        
        # 2. Создаем объекты страниц
        print("2. Создаем объекты Page Object...")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        # 3. Открываем сайт магазина
        print("3. Открываем сайт магазина...")
        login_page.open("https://www.saucedemo.com/")
        
        # 4. Авторизуемся как standard_user
        print("4. Авторизуемся как standard_user...")
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)  # Ждем загрузки
        
        # 5. Добавляем товары в корзину
        print("5. Добавляем товары в корзину...")
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)
            print(f"   Добавлен: {item}")
        
        # Проверяем количество в корзине
        cart_count = inventory_page.get_cart_count()
        print(f"   Товаров в корзине: {cart_count}")
        
        # 6. Переходим в корзину
        print("6. Переходим в корзину...")
        inventory_page.go_to_cart()
        time.sleep(1)
        
        # Проверяем товары в корзине
        cart_items = cart_page.get_item_names()
        print(f"   Товары в корзине: {cart_items}")
        
        # 7. Нажимаем Checkout
        print("7. Нажимаем кнопку Checkout...")
        cart_page.click_checkout()
        time.sleep(1)
        
        # 8. Заполняем форму данными
        print("8. Заполняем форму оформления заказа...")
        checkout_page.fill_shipping_info(
            first_name="Иван",
            last_name="Петров", 
            postal_code="123456"
        )
        print("   Данные заполнены: Иван Петров, индекс 123456")
        
        # 9. Нажимаем Continue
        print("9. Нажимаем Continue...")
        checkout_page.click_continue()
        time.sleep(1)
        
        # 10. Получаем итоговую стоимость
        print("10. Получаем итоговую стоимость...")
        total_amount = checkout_page.get_total_amount()
        print(f"   Итоговая сумма: ${total_amount}")
        
        # 11. Проверяем с помощью assert
        print("11. Проверяем итоговую сумму...")
        assert total_amount == "58.29", f"Expected $58.29, but got ${total_amount}"
        print(f"   ✓ Assert пройден! Сумма корректна: ${total_amount}")
        
        # 12. Нажимаем Finish (опционально)
        print("12. Завершаем заказ...")
        checkout_page.click_finish()
        time.sleep(1)
        
        # Проверяем что заказ завершен
        if checkout_page.is_order_complete():
            print("   ✓ Заказ успешно завершен!")
        
        print("\n" + "="*50)
        print("✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("="*50)
        
    except AssertionError as e:
        print(f"\n✗ ОШИБКА ПРОВЕРКИ: {e}")
        raise
    except Exception as e:
        print(f"\n✗ ОШИБКА ВО ВРЕМЯ ТЕСТА: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        # 13. Закрываем браузер
        if driver:
            print("\n13. Закрываем браузер...")
            driver.quit()
            print("   ✓ Браузер закрыт")

if __name__ == "__main__":
    test_sauce_demo_checkout()