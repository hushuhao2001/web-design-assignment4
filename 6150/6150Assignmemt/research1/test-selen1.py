from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("https://www.bbc.com/news")


    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2"))
    )

    rendered_html = driver.page_source
    print(rendered_html[:500])

finally:

    driver.quit()
