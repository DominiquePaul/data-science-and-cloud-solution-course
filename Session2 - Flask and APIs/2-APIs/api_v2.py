"""
In this script: Status codes and an example of what can wrong when using an API
"""

import requests

# Never save API keys in your code. You can get your own API key at
# https://rapidapi.com/fyhao/api/currency-exchange
API_KEY = "YOUR-API-KEY-HERE"

url = "https://currency-exchange.p.rapidapi.com/exchange"

# assume we omit the headers...
# headers = {
#     'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
#     'x-rapidapi-key': API_KEY
#     }

parameters = {"q":"1.0","from":"EUR","to":"USD"}

# we still dont get an error
r = requests.get(url,  params=parameters) #headers=headers)

# but the response was unsuccessful nevertheless as we can see in the status code
# have a look at this website to look up a status code
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
print(r.status_code)

print() # prints an empty line
print(r.json())
