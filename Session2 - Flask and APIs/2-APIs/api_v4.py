"""
This file links together with the api_v3 script and shows what __name__ ==
"__main__" is for and what can happen when it isnt used in certain circumstances
"""

from api_v3 import fx_request

if __name__ == "__main__":
    print("This is only executed if the script *itself* is being run")
    print(fx_request())
