"""
This script is used
"""

from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import time

# reminder: dont store your credentials like this, this is only for illustrative purpose
connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format("root", "MyP4ssword123!", "34.65.173.67", "3306", "webapp_data")
engine = create_engine(connect_string)

stores = ["Zurich", "Paris", "Berlin"]
items = {"Shirt": 50.0, "Trousers": 65.0, "Jumper": 80.0}

cols = ["Purchase_ID", "Location", "Item", "Amount", "Price", "Total"]
df = pd.DataFrame(columns=cols, data= np.zeros([0,6]))

for i in range(10):
    store = np.random.choice(stores)
    item = np.random.choice(list(items.keys()))
    price = items[item]
    amount = np.random.choice([1,2,3])
    total = price * amount
    row = [int(i), store, item, price, amount, total]
    new_row = pd.DataFrame(data=[row], columns=cols)
    df = df.append(new_row, ignore_index=True)

df.to_sql("shop_analytics", con=engine, if_exists="replace", index=False)


for i in range(60):
    print(i) if (i%10 == 0) else None
    store = np.random.choice(stores)
    item = np.random.choice(list(items.keys()))
    price = items[item]
    amount = np.random.choice([1,2,3])
    total = price * amount
    identifier = int(len(df)+i)
    row = [identifier, store, item, price, amount, total]
    new_row = pd.DataFrame(data=[row], columns=cols, index=[None])
    new_row.to_sql("shop_analytics", con=engine, if_exists="append", index=False)
    time.sleep(0.5)

pd.read_sql("shop_analytics", con=engine)
