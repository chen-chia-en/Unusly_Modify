import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

url = "https://app.disclosures.io/link/1482-Nightshade-Road-31-0ax3eu92"


# 無解錯誤訊息修正
options=Options()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver=webdriver.Chrome(options=options)
driver.get(url)

#Role
county_element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-role")))
select_county = Select(county_element)
select_county.select_by_value("Buyer")

#Name
Name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-name")))
Name.send_keys('Molly')

#Email
Email =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email")))
Email.send_keys("molly6825@gmail.com")

# work with agent ? NO
agent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form > div:nth-child(6) > label:nth-child(3) > i')))
agent.click()

submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-success')))
submit.click()

time.sleep(3)
driver.close()
time.sleep(3)

print("----over----")