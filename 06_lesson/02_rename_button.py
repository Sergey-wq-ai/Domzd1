from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://uitestingplayground.com/textinput")
    
    # Вводим текст и нажимаем кнопку
    driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
    driver.find_element(By.ID, "updatingButton").click()
    
    # Получаем новый текст кнопки
    text = driver.find_element(By.ID, "updatingButton").text
    print(f'("{text}")')