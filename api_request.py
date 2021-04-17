import requests
from api_key import key

def get_price_history(**kwargs):
    symbol = kwargs.get('symbol')
    url = f'https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory'

    params = {}

    params.update({'apikey' : key})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    return requests.get(url, params = params).json()
