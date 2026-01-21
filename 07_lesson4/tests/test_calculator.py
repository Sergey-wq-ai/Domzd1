import sys
import os
import time
from selenium import webdriver

# Add parent directory to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from pages.calculator_page import CalculatorPage


def test_calculator_with_delay():
    
    driver = None
    try:
        # 1. Create Chrome driver
        driver = webdriver.Chrome()
        
        # 2. Create page object
        calculator = CalculatorPage(driver)
        
        # 3. Open calculator page
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        
        # 4. Set delay to 45 seconds
        calculator.set_delay(45)
        
        # 5. Click buttons: 7 + 8 =
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')
        
        # 6. Wait for result (45 seconds + buffer)
        time.sleep(46)
        
        # 7. Get result
        result = calculator.get_result()
        
        # 8. Assert expected result
        assert result == "15", f"Expected 15, but got {result}"
        
    finally:
        # 9. Close browser
        if driver:
            driver.quit()


if __name__ == "__main__":
    test_calculator_with_delay()