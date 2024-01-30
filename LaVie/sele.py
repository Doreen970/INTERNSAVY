from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/blog/search")
    search_input = driver.find_element_by_name("q")
    search_input.send_keys("skin")

    search_input.send_keys(Keys.RETURN)
    time.sleep(4)

    assert "Search results for" in driver.page_source

finally:
    driver.quit()    

