#!/usr/bin/python2.7
# encoding: utf-8

__auteur__ = "Antonin Paillet"
__licence__ = "CC/BY-SA-NC"

import requests
import numpy as np
import gnuplotlib as gp
import json
import time

# FROM BTC to USD // HistoHour [72 hours]

def requestData():
    r = requests.get('https://min-api.cryptocompare.com/data/histohour?'
                     'fsym=BTC&tsym=USD&limit=72&aggregate=1&e=CCCAGG')
    jj = json.loads(r.text)  # loads data into json format
    price = [el['close'] for el in jj['Data']]  # extract the price as a list
    _time = [el['time'] for el in jj['Data']]   # extract the time as a list
    return price, _time

while True:
    y_price, x_time = requestData()
    y = np.array(y_price)
    x = np.arange(-73, 0)
    gp.plot(np.flipud(x), y, _with='lines', terminal='dumb 100, 30', title='BTC to USD exchange rate (72h)')
    time.sleep(360) # Updates every hour
