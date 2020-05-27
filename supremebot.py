import requests
import json
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2



###########################################################################
category = "Jackets"
keyword_1 = "Shiny"
keyword_2 = "Reversible"
keyword_color = "Black"
keyword_size = "Medium"
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
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257',                               
'Referer': 'http://www.supremenewyork.com/mobile'  
}


stock_response = requests.get(stock_url,headers=supreme_headers)
stock_data = stock_response.json()


products = stock_data['products_and_categories'][category]

for product in products:
    if keyword_1 in product['name'] and keyword_2 in product['name']:
        productID = product['id']
        break


product_url = "http://www.supremenewyork.com/shop/"+str(productID)+".json"
product_response = requests.get(product_url,headers=supreme_headers)
product_data = product_response.json()

styles = product_data['styles']


for color in styles:
    if keyword_color in color['name']:
        colorID = color['id']
        sizes = color['sizes']
        for size in sizes:
            if keyword_size in size['name']:
                sizeID = size['id']
                break
        break

print(colorID)
print(sizeID)

session = requests.Session()

atc_url = "http://www.supremenewyork.com/shop/"+str(productID)+"/add.json"
print(atc_url)

atc_headers = {                                                                                                                                      
    'Content-Type':      'application/x-www-form-urlencoded',                                                                                                                                                                                                                                                                                                                                                           
    'User-Agent':        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'                           
}

atc_data = {
    'st' : colorID,
    's' : sizeID,
    'qty': '1'
}
print("adding to cart")
genCheckout = session.post(atc_url,data=atc_data,headers=atc_headers)


checkoutpage = session.get("https://www.supremenewyork.com/mobile/#checkout")
checkoutUrl = "https://www.supremenewyork.com/checkout.json"

checkoutHeaders = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.supremenewyork.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.supremenewyork.com/mobile/',
    'TE': 'Trailers'
}

checkoutInfo = {
        'authenticity_token': 'F3eqx3dGqdVfwD0jY3bzeWwfbAgD6eOrwLAIdu+7B3mf2ndhBjlqZBDRdKU1VgRWAHHfkazqegHfB/V2Dn4Ziw==',
        'order[billing_name]':      'anon mous',                              # FirstName LastName
        'cerear':                   'RMCEAR',
        'order[email]':             'anon@mailinator.com',                    # email@domain.com
        'order[tel]':               '999-999-9999',                           # phone-number-here
        'order[billing_address]':   '123 Seurat lane',                        # your address
        'order[billing_address_2]': '',
        'order[billing_zip]':       '90210',                                  # zip code
        'order[billing_city]':      'Beverly Hills',                          # city
        'order[billing_state]':     'CA',                                     # state
        'order[billing_country]':   'USA',                                    # country
        'same_as_billing_address':  '1',
        'store_credit_id':          '',
        'riearmxa':                 '9999 9999 9999 9999',                    # credit card number
        'credit_card[month]':       '01',                                     # expiration month
        'credit_card[year]':        '2026',                                   # expiration year
        'credit_card[meknk]':       '123',                                    # cvc/cvv
        'credit_card[vval]':        '',
        'order[terms]':             '0',
        'order[terms]':             '1',
        'g-recaptcha-response': '03AERD8Xpl2jE4MzoGNQE3vRvMTPRsl4ZgKxXc6oYrAp5xLsmKlJwwjLi4yKz1OFLnQaRAN4Pf648oxKw6V4DtWMwFmHmpDwehD49IUU3PrqMfoilT0ba-jcB3ws9h9FPk-BQPdr6lN_I1Ez8-y5k20tYazTxRlIa1mtPtQGXXry2m2k0aIpWdQrCnWglnIAEEQvk52pFylWZVPmNOzfhCVedF_dWA1VmZVOBg5Q3_6KZgI1ZiSZDTzqxK7SRjQdJewZ1Kx-6DcdXht7xxsp5ZM7LInwYIHNwtQyJSdJ6qoQ9f830YeE8PZIxI0eRLgUyX0T5UkJIB4Y_Eg0mm0J05R8-0_OC3j36XYv0auTI6fuCGpyayB1qZT3oPrJqfYzsxdmKw-xhh42XXy8rm3QEJ__HQKKMyHHTYOA'
    }
    

print("checking out")
checkout = session.post(checkoutUrl,data=checkoutInfo,headers=checkoutHeaders)

print(checkout.json())


