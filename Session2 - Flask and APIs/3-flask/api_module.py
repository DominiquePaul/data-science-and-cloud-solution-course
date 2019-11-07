"""
This script wraps some of our learnings from module 2 into a function that can
be called as a package in the flask_v1 script
"""

import requests

# Never save API keys in your code. You can get your own API key at
# https://rapidapi.com/fyhao/api/currency-exchange
RAPID_API_KEY = "YOUR-API-KEY-HERE"

def fx_request(quantity="1.0", curr_origin="EUR", curr_dest="USD"):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_KEY
        }

    # the parameters contain information about the query itself: what are we asking for?
    parameters = {"q":quantity,"from":curr_origin,"to":curr_dest}

    r = requests.get(url, headers=headers, params=parameters)

    return r.text

# this line is used for reference in the script api_v3
print("Hello")

if __name__ == "__main__":
    print(fx_request())
    print(fx_request(curr_origin="EUR", curr_dest="SEK"))
