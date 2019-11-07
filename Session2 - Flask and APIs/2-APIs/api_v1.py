"""
Introduction to requests. Here we briefly explore how to get data from an API
and use it for our own application. APIs are extremenly useful to add content,
functionality or other features to you own application without having to take
care of writing parts of the code yourself

More information on APIs and how the request package works:
https://www.youtube.com/watch?v=tb8gHvYlCFs

Source of the API used in this script:
https://rapidapi.com/fyhao/api/currency-exchange


To run the script you might have to run the following commands in your terminal
first. If you have installed python with anaconda then replace 'pip' with 'conda'

pip install requests
"""

# the requests package allows us to call http application interface in only one command
import requests

# the URL tells the program where we want to send our request
url = "https://currency-exchange.p.rapidapi.com/exchange"

# Never save API keys in your code. You can get your own API key at
# https://rapidapi.com/fyhao/api/currency-exchange
API_KEY = "YOUR-API-KEY-HERE"

# headers include important information to be sent with the message but which
# do not form part of the request itself. In our case, they contain information
# about the resource to be fetched and 'who' is asking for it (API key)
headers = {
    'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

# the parameters contain information about the query itself: what are we asking for?
parameters = {"q":"1.0","from":"EUR","to":"USD"}

r = requests.get(url, headers=headers, params=parameters)

# if we just print the response it doesnt seem that we're getting much information
print(r)

# one trick to see what we can do with an object in python is to call the dir() method
print(dir(r))
## some examples of what we might try
# the query sent (notice hwo the parameters got added to the url)
r.url
# also not what were looking for
r.request
# the status code tells us whether our request was successful
# If you run into errors, you can check out all status codes here:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
r.status_code
# finally what we were looking for
r.text
# but this is in text only and difficult to read out information if the response
# is longer. so what we normally use is .json() which gives us the response in
# a python dicitonary format
r.json()

# we print out the result
print("The exchange rate of the euro to the dollar is: {}".format(r.json()))
