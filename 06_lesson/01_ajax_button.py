from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    
    # Нажимаем кнопку
    driver.find_element(By.ID, "ajaxButton").click()
    
    # Ждем появления текста и получаем его
    text = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    ).text
    
    # Выводим в требуемом формате
    print(f'("{text}")')
    
finally:
    driver.quit()