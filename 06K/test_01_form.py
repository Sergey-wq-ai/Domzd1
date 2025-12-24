from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Edge()
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Сергей")
    driver.find_element(By.NAME, "last-name").send_keys("Жадеев")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Самара")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    # Нажимаем кнопку
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    # Ждем появления красного подсвечивания у Zip code
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.danger")))
    
    # Проверяем Zip code (красный)
    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
    
    # Проверяем остальные поля (зеленые)
    fields = ["first-name", "last-name", "address", "e-mail", "phone",
              "city", "country", "job-position", "company"]
    
    for field_id in fields:
        # Ждем пока каждое поле станет зеленым
        wait.until(lambda d: "success" in d.find_element(By.ID, field_id).get_attribute("class"))
        assert "success" in driver.find_element(By.ID, field_id).get_attribute("class")
    
    driver.quit()

if __name__ == "__main__":
    test_form()