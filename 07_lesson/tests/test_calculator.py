import sys
import os

# Добавляем родительскую папку в путь Python
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Теперь импортируем
try:
    from pages.calculator_page import CalculatorPage
    print("✓ Импорт CalculatorPage успешен")
except ImportError as e:
    print(f"✗ Ошибка импорта: {e}")
    # Покажем где ищем
    print(f"Текущая папка: {current_dir}")
    print(f"Родительская папка: {parent_dir}")
    print(f"sys.path: {sys.path}")
    exit(1)

from selenium import webdriver
import time

print("=== ТЕСТ КАЛЬКУЛЯТОРА ===")

try:
    # 1. Создаем драйвер
    print("1. Запускаем Chrome...")
    driver = webdriver.Chrome()
    
    # 2. Создаем объект страницы
    print("2. Создаем CalculatorPage...")
    calculator = CalculatorPage(driver)
    
    # 3. Открываем страницу
    print("3. Открываем страницу калькулятора...")
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # 4. Устанавливаем задержку
    print("4. Устанавливаем задержку 3 секунды...")
    calculator.set_delay(3)
    
    # 5. Нажимаем кнопки 7 + 8 =
    print("5. Вычисляем 7 + 8...")
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')
    
    # 6. Ждем результат
    print("6. Ждем результат (5 секунд)...")
    time.sleep(5)
    
    # 7. Получаем результат
    result = calculator.get_result()
    print(f"7. Результат: {result}")
    
    # 8. Проверяем
    if result == "15":
        print("✓ ТЕСТ ПРОЙДЕН! Результат верный: 15")
    else:
        print(f"✗ ТЕСТ НЕ ПРОЙДЕН! Ожидалось 15, получено {result}")
        
except Exception as e:
    print(f"✗ Ошибка: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    # 9. Закрываем браузер
    try:
        driver.quit()
        print("✓ Браузер закрыт")
    except:
        pass