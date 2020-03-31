from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import sys
import time
from datetime import datetime
def bitcoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD',
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'cea8c349-5010-4b02-8e1e-818553a599a6',
        }
        
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)  # storing json response in variable
        
        for item in data['data']:
            price=item['quote']['USD']['price']
            price2=int(price)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return(price2)
def main():
    max_limit=6000 
    bitcoin_history=[]
    i=0
    while(i<5):
        price=bitcoin_price()
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
        date=str(date_time)
        price2=int(price)
        bitcoin_history.append({'value1': date, 'value2': price2})
        if price2 > max_limit:  #when price exceeds to max limit sends emergency notification
            price_data={'value1':price2}  #formatting the data to ifttt format
            ifttt_webhook_url = 'https://maker.ifttt.com/trigger/Bitcoin_Emergency_Price/with/key/k_imIB2s8GDN0fFTJ529yANDqBV9UmwxObjwvp2nrPR' #ifttt url for emergency price notification
            requests.post(ifttt_webhook_url,price_data)
        i+=1
        time.sleep(60)
    rows=[]
    if len(bitcoin_history) == 5: #loop executes when length of array is equal to 5
        for i in bitcoin_history: #getting each value of array and iterrating 
            date=i['value1']  #here data in array is in dictionary format, using keys to retrive the data
            price=i['value2']
            row = '{}: $<b>{}</b><br>'.format(date, price)  #formatting the data accourdingly 
            rows.append(row)      #appending the data to an array 
            data={'value1':''.join(rows)}
        ifttt_webhook_url = 'https://maker.ifttt.com/trigger/Bitcoin_Tracker/with/key/k_imIB2s8GDN0fFTJ529yANDqBV9UmwxObjwvp2nrPR'
        requests.post(ifttt_webhook_url,json=data)  #passing the formatted value in json format
        bitcoin_history=[]

main()


