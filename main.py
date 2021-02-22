from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("https://www.autohero.com/de/search/")
driver.maximize_window()

yearFilter = driver.find_element_by_xpath(
    "/html/body/div[1]/div/main/div/div[1]/div[1]/div[3]/button")
yearFilter.click()

year = driver.find_element_by_xpath(
    "/html/body/div[1]/div/main/div/div[1]/div/div[3]/div/div/div/div[1]/select[@id='rangeStart']/option[text()='2015']")
year.click()

sortBy = driver.find_element_by_xpath(
    "/html/body/div[1]/div/main/div/div[1]/div[1]/select[@id='sortBy']/option[text()='Höchster Preis']")
sortBy.click()

year = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[1]/div/div/div/div[1]/a/div[2]/ul/li[1]")))

priceElement1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[1]/div/div/div/div[1]/a/div[2]/div[1]/div")))

priceElement2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[1]/div/div/div/div[2]/a/div[2]/div[1]/div")))

price1 = priceElement1.text.replace(" €", "")
price1 = price1.replace(".", "")

price2 = priceElement2.text.replace("€", "")
price2 = price2.replace(".", "")

assert int(year.text) >= 2015
assert int(price1) >= int(price2)

driver.quit()
