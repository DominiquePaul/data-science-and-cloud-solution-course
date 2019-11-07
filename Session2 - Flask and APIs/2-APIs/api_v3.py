"""
Wrapping our work into a function
"""
import requests

# Never save API keys in your code. You can get your own API key at
# https://rapidapi.com/fyhao/api/currency-exchange
API_KEY = "YOUR-API-KEY-HERE"

def fx_request(quantity="1.0", curr_origin="EUR", curr_dest="USD"):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
        }

    # the parameters contain information about the query itself: what are we asking for?
    parameters = {"q":quantity,"from":curr_origin,"to":curr_dest}
    r = requests.get(url, headers=headers, params=parameters)

    return r.text

# this line is used for reference in the script api_v3
print("This is coming from the api_v3 script")
# print(fx_request(curr_origin="EUR", curr_dest="SEK"))

# What does this condition do?
# this command only runs when the script itself is being executed and not, for
# example when this script is loaded by another package
# More: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    print(fx_request())
