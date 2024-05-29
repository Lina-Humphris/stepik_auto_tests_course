from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return str(int(x)+int(y))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap[id = num1]")
    y_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap[id = num2]")
    x, y = x_element.text, y_element.text
    z = calc(x, y)


    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(z)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()