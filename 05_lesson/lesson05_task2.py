from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Небольшая пауза для загрузки страницы
    time.sleep(2)
    
    # Кликнуть на синюю кнопку (ищем по классу кнопки)
    # Используем XPath для большей надежности
    blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
    blue_button.click()
    
    # Пауза, чтобы увидеть результат
    time.sleep(2)
    
    print("Скрипт выполнен успешно!")
    
finally:
    # Закрыть браузер
    driver.quit()