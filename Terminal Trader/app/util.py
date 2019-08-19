import requests
from requests import Response
from hashlib import sha256

API_KEY = ''

def hash_password(password,salt="salt"):
    m = sha256()
    encoded_password = password.encode() 
    m.update(encoded_password)
    m.update(salt)
    return m.hexdigest()

def get_price(ticker):
    global API_KEY
    iex_base = "https://cloud.iexapis.com/stable"
    quote_endpoint = iex_base + '/stock/{}/quote?token='
    try:
        response = requests.get(quote_endpoint.format(ticker) + API_KEY)
        current_price = response.json()['latestPrice']
        return float(current_price)
    except:
        return None

def set_token():
    with open('tokenfile.txt','r') as f:
        token = f.read()
        return token 


if __name__ == "__main__":
    API_KEY - set_token()
    print(get_price(self))