import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("../data/avocado.csv", index_col=0)
column_name_replacements = {"Total Volume":"TotalVolume",
                            "Total Bags": "TotalBags",
                            "Small Bags": "SmallBags",
                            "Large Bags": "LargeBags",
                            "XLarge Bags": "XLargeBags"}
df.rename(column_name_replacements, axis=1, inplace=True)
df.head()


connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format("root", "SQLp4ssword12397!", "34.65.70.52", "3306", "my_app_data")

engine = create_engine(connect_string)
engine


df.to_sql("avocado_data", engine, if_exists="replace")

sql_query = "select * from avocado_data;"
df_from_cloud = pd.read_sql_query(sql_query, engine)

df.columns

row_values = {"AveragePrice":2.70, "Total Volume": 1000, "region": "St. Gallen"}
df_from_row = pd.DataFrame(row_values, index=[1])
df_from_row.to_sql("avocado_data", engine, if_exists="append")


sql_query = "select * from avocado_data;"
df_from_cloud = pd.read_sql_query(sql_query, engine)
df_from_cloud.tail()

sql_query = "show tables;"
result = engine.execute(sql_query)
result.fetchall()

sql_query = "select * from avocado_data limit 5;"
result = engine.execute(sql_query)
result.fetchall()


df_new = df[1:10].copy()
# create a new sql table
df_new.to_sql("df_new", engine, if_exists="replace")

sql_update_query = "UPDATE def_new SET TotalVolume = 200 WHERE LargeBags > 200"
result = engine.execute(sql_update_query)

delete_query = "DELETE FROM df_new WHERE LargeBags > 200"
result = engine.execute(delete_query)
