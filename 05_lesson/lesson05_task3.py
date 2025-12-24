from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка драйвера Firefox
try:
    print("Инициализация драйвера Firefox...")
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    # Увеличиваем время ожидания
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    
    print("Открываем страницу...")
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Проверка, что страница загрузилась
    print(f"Текущий URL: {driver.current_url}")
    print(f"Заголовок страницы: {driver.title}")
    
    # Даем время на полную загрузку
    time.sleep(3)
    
    # Найти поле ввода
    print("Ищем поле ввода...")
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Ввести текст Sky
    print("Вводим текст 'Sky'...")
    input_field.send_keys("Sky")
    time.sleep(1)
    
    # Очистить поле
    print("Очищаем поле...")
    input_field.clear()
    time.sleep(1)
    
    # Ввести текст Pro
    print("Вводим текст 'Pro'...")
    input_field.send_keys("Pro")
    time.sleep(1)
    
    print("Скрипт выполнен успешно!")
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    print(f"Тип ошибки: {type(e).__name__}")
    
finally:
    # Закрыть браузер
    try:
        driver.quit()
        print("Браузер закрыт.")
    except:
        pass