from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu time")
# print(type(dates))
# print(dates[0].text)

names= driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")
# print(type(names))
# print(names[0].text)

dictionary = {}

for index, (item1, item2) in enumerate(zip(dates, names)):
    dictionary[index] = {
            "time": dates[index].text,
            "name": names[index].text,       
    }

print(dictionary)

