# from time import sleep


from selenium import webdriver
# from selenium.webdriver.common.keys import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

# from selenium.webdriver.remote.webelement import WebElement


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://peletok-staging.ravtech.co.il")
wait = WebDriverWait(driver, timeout=20)

elenent = wait.until(ec.element_to_be_clickable(locator=(By.ID, "usernameId"))).send_keys("peletok0")
# elenent.send_keys("peletok0")
elenent = wait.until(ec.element_to_be_clickable(locator=(By.ID, "passwordId"))).send_keys("pass0")
# elenent.send_keys("pass0")
elenent = wait.until(ec.element_to_be_clickable(locator=(By.ID, "btnLogin"))).click()  #  id = כפתור של התחבר
# elenent.click()
elenent = wait.until(ec.element_to_be_clickable(locator=(By.ID, "id94Link"))).click()   #  id = כפתור של סלקום
# elenent.click()
print("befor")

elenent = wait.until(ec.element_to_be_clickable(locator=(By.CLASS_NAME, "productName")))
print("after")

print(elenent.text)
