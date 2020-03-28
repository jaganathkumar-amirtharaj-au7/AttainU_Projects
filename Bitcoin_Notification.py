from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import sys
import time
from datetime import datetime

max_limit=6000      #setting maxlimit for emergency notification
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' #URL for coincap market
parameters = {  #setting parameters for retriving data from coincapmarket
  'start':'1',
  'limit':'1',  #setting limit to 1 as the bitcoin is first value
  'convert':'USD',  #setting USD to get value in dollors
  
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'cea8c349-5010-4b02-8e1e-818553a599a6',  #api key for coincapmaret
}

session = Session()
session.headers.update(headers)

try:
  
  response = session.get(url, params=parameters)
  data = json.loads(response.text)  # storing json response in variable
  now = datetime.now()
  date_time = now.strftime("%m/%d/%Y,%H:%M:%S") #getting current date time and formating it in month,date,year
  date=str(date_time)


  for item in data['data']: #getting data from json and using for loop to iterating the data
    price=item['quote']['USD']['price'] #getting price value from json
    price2=int(price) # converting the float to integer value.
    if price2 > max_limit:  #when price exceeds to max limit sends emergency notification
          price_data={'value1':price2}  #formatting the data to ifttt format
          ifttt_webhook_url = 'https://maker.ifttt.com/trigger/Bitcoin_Emergency_Price/with/key/k_imIB2s8GDN0fFTJ529yANDqBV9UmwxObjwvp2nrPR' #ifttt url for emergency price notification
          requests.post(ifttt_webhook_url,price_data) 
    bitcoin_history=[]  #array for storing the values
    for i in range(0,5):  #using for looping just five times
        bitcoin_history.append({'value1': date, 'value2': price2})  #appending the values to array
        rows=[]
        if len(bitcoin_history) == 5: #loop executes when length of array is equal to 5
            for i in bitcoin_history: #getting each value of array and iterrating 
                date=i['value1']  #here data in array is in dictionary format, using keys to retrive the data
                price=i['value2']
                row = '{}: $<b>{}</b><br>'.format(date, price)  #formatting the data accourdingly 
                rows.append(row)      #appending the data to an array 
                data={'value1':''.join(rows)} #joining the array to ifttt format
                
            ifttt_webhook_url = 'https://maker.ifttt.com/trigger/Bitcoin_Tracker/with/key/k_imIB2s8GDN0fFTJ529yANDqBV9UmwxObjwvp2nrPR'
            requests.post(ifttt_webhook_url,json=data)  #passing the formatted value in json format
            bitcoin_history=[]  #finally setting the array list to null, so when loop is executed again, previous data doesn't interfere
                 
        time.sleep(1) #here we are using sleep to set time interval of execution
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)






