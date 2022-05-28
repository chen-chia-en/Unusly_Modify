from selenium import webdriver
import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
url = 'https://c.8891.com.tw/{}/{}/Summary.html'

# Selenium 作法
# https://c.8891.com.tw/
#無解錯誤訊息修正
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
driver=webdriver.Chrome(options=options)
  
# first tab
info = {'bmw':'1-series-coupe', 'ds':'3','alfa-romeo':'147', 'ferrari':'458', 'fiat':'panda','honda':'accord'}
for brand, cartype in info.items():
    if brand =='bmw':
        driver.get(url.format(brand, cartype))

        res = requests.get(url.format(brand, cartype),headers=headers).text
        soup = BeautifulSoup(res, 'html.parser')
        name = soup.select('#container > div.wrap-width.clearfix.mt10.viewIndexSummarypageTop > div > div.summary-top-main.fl > h1')[0].text
        print('car: ', name)
    else:
        driver.execute_script("window.open('about:blank','{}tab');".format(brand))
        driver.switch_to.window(brand+'tab')
        driver.get(url.format(brand, cartype))
        res = requests.get('https://c.8891.com.tw/{}/{}/Summary.html'.format(brand, cartype),headers=headers).text
        soup = BeautifulSoup(res, 'html.parser')
        name = soup.select('#container > div.wrap-width.clearfix.mt10.viewIndexSummarypageTop > div > div.summary-top-main.fl > h1')[0].text
        print('car: ', name)
driver.quit()

# ***Only Requests 作法
# info = {'bmw':'1-series-coupe', 'ds':'3','alfa-romeo':'147', 'ferrari':'458', 'fiat':'panda','honda':'accord'}
# for brand, cartype in info.items():
#     res = requests.get(url.format(brand, cartype),headers=headers).text
#     soup = BeautifulSoup(res, 'html.parser')
#     name = soup.select('#container > div.wrap-width.clearfix.mt10.viewIndexSummarypageTop > div > div.summary-top-main.fl > h1')[0].text
#     print('car: ', name)