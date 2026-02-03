import sys
import os
import time
import allure
import pytest

# Добавляем родительскую папку в путь Python для импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полное оформление заказа с тремя товарами")
@allure.description("""
Тест проверяет полный процесс оформления заказа:
1. Авторизация
2. Добавление 3 товаров в корзину
3. Переход в корзину
4. Заполнение данных доставки
5. Проверка итоговой суммы
6. Завершение заказа
""")
def test_sauce_demo_checkout():
    """Тест для интернет-магазина Sauce Demo."""
    driver = None
    
    try:
        with allure.step("1. Инициализация драйвера Firefox"):
            print("1. Запускаем Firefox...")
            driver = webdriver.Firefox()
            driver.implicitly_wait(10)
        
        with allure.step("2. Создание объектов Page Object"):
            print("2. Создаем объекты Page Object...")
            login_page = LoginPage(driver)
            inventory_page = InventoryPage(driver)
            cart_page = CartPage(driver)
            checkout_page = CheckoutPage(driver)
        
        with allure.step("3. Открытие сайта магазина"):
            print("3. Открываем сайт магазина...")
            login_page.open("https://www.saucedemo.com/")
        
        with allure.step("4. Авторизация как standard_user"):
            print("4. Авторизуемся как standard_user...")
            login_page.login("standard_user", "secret_sauce")
            time.sleep(2)
        
        with allure.step("5. Добавление товаров в корзину"):
            print("5. Добавляем товары в корзину...")
            items_to_add = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt", 
                "Sauce Labs Onesie"
            ]
            
            for item in items_to_add:
                inventory_page.add_item_to_cart(item)
                print(f"   Добавлен: {item}")
            
            cart_count = inventory_page.get_cart_count()
            print(f"   Товаров в корзине: {cart_count}")
            
            with allure.step("Проверка количества товаров в корзине"):
                assert cart_count == 3, f"Ожидалось 3 товара, но найдено {cart_count}"
        
        with allure.step("6. Переход в корзину"):
            print("6. Переходим в корзину...")
            inventory_page.go_to_cart()
            time.sleep(1)
            
            cart_items = cart_page.get_item_names()
            print(f"   Товары в корзине: {cart_items}")
            
            with allure.step("Проверка товаров в корзине"):
                assert len(cart_items) == 3, "В корзине должно быть 3 товара"
        
        with allure.step("7. Нажатие кнопки Checkout"):
            print("7. Нажимаем кнопку Checkout...")
            cart_page.click_checkout()
            time.sleep(1)
        
        with allure.step("8. Заполнение формы оформления заказа"):
            print("8. Заполняем форму оформления заказа...")
            checkout_page.fill_shipping_info(
                first_name="Иван",
                last_name="Петров", 
                postal_code="123456"
            )
            print("   Данные заполнены: Иван Петров, индекс 123456")
        
        with allure.step("9. Нажатие кнопки Continue"):
            print("9. Нажимаем Continue...")
            checkout_page.click_continue()
            time.sleep(1)
        
        with allure.step("10. Получение итоговой стоимости"):
            print("10. Получаем итоговую стоимость...")
            total_amount = checkout_page.get_total_amount()
            print(f"   Итоговая сумма: ${total_amount}")
            
            with allure.step("Проверка итоговой суммы"):
                assert total_amount == "58.29", f"Ожидалось $58.29, но получено ${total_amount}"
                print(f"   ✓ Сумма корректна: ${total_amount}")
        
        with allure.step("11. Завершение заказа"):
            print("11. Завершаем заказ...")
            checkout_page.click_finish()
            time.sleep(1)
            
            with allure.step("Проверка завершения заказа"):
                assert checkout_page.is_order_complete(), "Заказ не был завершен успешно"
                print("   ✓ Заказ успешно завершен!")
        
        print("\n" + "="*50)
        print("✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("="*50)
        
    except AssertionError as e:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_failure", 
                      attachment_type=allure.attachment_type.PNG)
        print(f"\n✗ ОШИБКА ПРОВЕРКИ: {e}")
        raise
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_error", 
                      attachment_type=allure.attachment_type.PNG)
        print(f"\n✗ ОШИБКА ВО ВРЕМЯ ТЕСТА: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        with allure.step("12. Закрытие браузера"):
            if driver:
                print("\n12. Закрываем браузер...")
                driver.quit()
                print("   ✓ Браузер закрыт")


if __name__ == "__main__":
    test_sauce_demo_checkout()