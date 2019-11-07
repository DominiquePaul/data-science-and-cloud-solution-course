# Run either of the following commands in your terminal to install the package
# conda install requests
# conda install dotenv

import requests
import os
from dotenv import load_dotenv

# Never save API keys in your code. You can get your own API key at
# https://rapidapi.com/fyhao/api/currency-exchange
RAPID_API_KEY = "YOUR-API-KEY-HERE"

# other ways to load environment variables
# RAPID_API_KEY = load_dotenv(dotenv_path="./secrets.env", verbose=True)
# RAPID_API_KEY = os.environ["qRAPID_API_KEY"]
querystring = {"q":"1.0","from":"EUR","to":"USD"}


headers = {
    'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

requests.get("https://currency-exchange.p.rapidapi.com/exchange")

from sklearn import datasets
data = datasets.load_boston()
data


import requests


nasa_api_key = "YOUR-API-KEY-HERE"

headers = {"api_key": nasa_api_key}

url = "https://api.nasa.gov/planetary/apod"

r = requests.get(url, params=headers)

r.json()

print(r.json()["explanation"])
image_url = r.json()["url"]

# show image

from PIL import Image
img = Image.open(requests.get(image_url, stream=True).raw)
img.show()
