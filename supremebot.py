import requests
import json
from selenium import webdriver



###########################################################################
category = "Jackets"
keyword_1 = "Gonz"
keyword_2 = "Coaches"
keyword_color = "Violet"
keyword_size = "XLarge"
###########################################################################
productID = ""
colorID = ""
sizeID = ""


###########################################################################
stock_url = "http://www.supremenewyork.com/mobile_stock.json"
supreme_headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Host": "www.supremenewyork.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
}

stock_response = requests.get(stock_url,headers=supreme_headers)
stock_data = stock_response.json()
print(stock_response.text)

products = stock_data['products_and_categories'][category]

for product in products:
    if keyword_1 in product['name'] and keyword_2 in product['name']:
        productID = product['id']
        break

product_url = "http://www.supremenewyork.com/shop/"+str(productID)

colors = products['styles']

for color in colors:
    if keyword_color in color['name']:
        colorID = color['id']
        sizes = color['sizes']
        for size in sizes:
            if keyword_size in size['name']:
                sizeID = size['id']
                break
        break


session = requests.Session()

atc_url = "http://www.supremenewyork.com/shop/"+str(productID)+"/add.json"

atc_headers = {
"Accept": "application/json",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
"Host": "www.supremenewyork.com",
"Origin": "http://www.supremenewyork.com",
"Referer": "http://www.supremenewyork.com/mobile/",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}

atc_data = {
    "size" : sizeID,
    "style" : colorID,
    "qty": "1"
}

driver = webdriver.Firefox()

driver.get("http://www.supremenewyork.com/shop/cart")

driver.delete_all_cookies()

for cookie in atc_cookies:
    driver.add_cookie({"name":cookie,"value":atc_cookies[cookie]})

driver.get("https://www.supremenewyork.com/checkout")

driver.find_element_by_id("order_billing_name").send_keys("John Lennon")
driver.find_element_by_id("order_email").send_keys("Johnlennon@gmail.com")
driver.find_element_by_id("order_tel").send_keys("7024818150")
driver.find_element_by_id("bo").send_keys("1 Mcdonalds Way")
driver.find_element_by_id("oba3").send_keys("Room 470")
driver.find_element_by_id("order_billing_zip").send_keys("01354")
driver.find_element_by_id("order_billing_city").send_keys("Mount Hermon")
driver.find_element_by_id("order_billing_country").send_keys("USA")
driver.find_element_by_id("nnaerb").send_keys("4792131241818123")
driver.find_element_by_id("credit_card_month").send_keys("08")
driver.find_element_by_id("credit_card_year").send_keys("2021")
driver.find_element_by_id("orcer").send_keys("123")








