from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(3)
    
    # Заполняем форму
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # Нажимаем кнопку
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    
    # Получаем текст сообщения
    message = driver.find_element(By.ID, "flash").text
    message = message.replace('×', '').strip()
    
    print(f"Сообщение: {message}")
    
finally:
    # Закрываем браузер
    driver.quit()