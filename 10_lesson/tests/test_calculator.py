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
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест калькулятора с задержкой вычислений")
@allure.description("""
Тест проверяет работу калькулятора с настраиваемой задержкой:
1. Открытие страницы калькулятора
2. Установка задержки вычислений
3. Выполнение операции 7 + 8
4. Ожидание результата
5. Проверка правильности вычислений
""")
def test_calculator_with_delay():
    """Тест калькулятора с задержкой вычислений."""
    driver = None
    
    try:
        with allure.step("1. Инициализация драйвера Chrome"):
            driver = webdriver.Chrome()
            driver.implicitly_wait(5)
        
        with allure.step("2. Создание объекта CalculatorPage"):
            calculator = CalculatorPage(driver)
        
        with allure.step("3. Открытие страницы калькулятора"):
            driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
            
            with allure.step("Проверка загрузки калькулятора"):
                assert calculator.is_calculator_loaded(), "Калькулятор не загрузился"
        
        with allure.step("4. Установка задержки 45 секунд"):
            calculator.set_delay(45)
        
        with allure.step("5. Выполнение операции 7 + 8 ="):
            calculator.perform_operation("7+8=")
        
        with allure.step("6. Ожидание результата (45 секунд + буфер)"):
            print("Ожидание 46 секунд для получения результата...")
            time.sleep(46)
        
        with allure.step("7. Получение и проверка результата"):
            result = calculator.get_result()
            print(f"Получен результат: {result}")
            
            with allure.step(f"Проверка что результат равен '15'"):
                assert result == "15", f"Ожидалось 15, но получено {result}"
                print(f"✓ Результат корректен: {result}")
        
        print("\n" + "="*50)
        print("✓ ТЕСТ КАЛЬКУЛЯТОРА ПРОЙДЕН УСПЕШНО!")
        print("="*50)
        
    except AssertionError as e:
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_failure", 
                          attachment_type=allure.attachment_type.PNG)
        print(f"\n✗ ОШИБКА ПРОВЕРКИ: {e}")
        raise
    except Exception as e:
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_error", 
                          attachment_type=allure.attachment_type.PNG)
        print(f"\n✗ ОШИБКА ВО ВРЕМЯ ТЕСТА: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        with allure.step("8. Закрытие браузера"):
            if driver:
                print("\n8. Закрываем браузер...")
                driver.quit()
                print("   ✓ Браузер закрыт")


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Быстрый тест калькулятора")
@allure.description("Быстрый тест калькулятора без длительной задержки.")
def test_calculator_quick():
    """Быстрый тест калькулятора без длительной задержки."""
    driver = None
    
    try:
        with allure.step("1. Инициализация драйвера"):
            driver = webdriver.Chrome()
            driver.implicitly_wait(5)
        
        with allure.step("2. Создание объекта CalculatorPage"):
            calculator = CalculatorPage(driver)
        
        with allure.step("3. Открытие страницы калькулятора"):
            driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        
        with allure.step("4. Установка минимальной задержки"):
            calculator.set_delay(1)
        
        with allure.step("5. Выполнение простой операции"):
            calculator.perform_operation("2+3=")
            time.sleep(2)  # Короткая задержка
        
        with allure.step("6. Проверка результата"):
            result = calculator.get_result()
            
            with allure.step("Проверка что результат равен '5'"):
                assert result == "5", f"Ожидалось 5, но получено {result}"
                print(f"✓ Быстрый тест пройден: 2 + 3 = {result}")
        
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    test_calculator_with_delay()