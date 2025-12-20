from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# Настройка драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")
    
    # Небольшая пауза для загрузки страницы
    time.sleep(2)
    
    # Кликнуть на синюю кнопку (ищем по классу)
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    
    # Пауза, чтобы увидеть результат
    time.sleep(2)
    
    # Обработка всплывающего окна (если появится)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    
    print("Скрипт выполнен успешно!")
    
finally:
    # Закрыть браузер
    driver.quit()