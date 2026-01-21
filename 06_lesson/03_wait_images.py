from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ждем, когда загрузятся картинки (проверяем, что у первой картинки есть src)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img[src*='award']"))
    )
    
    # Получаем все картинки
    all_images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    
    # Получаем src третьей картинки (индекс 2)
    src = all_images[2].get_attribute("src")
    
    print(f'("{src}")')