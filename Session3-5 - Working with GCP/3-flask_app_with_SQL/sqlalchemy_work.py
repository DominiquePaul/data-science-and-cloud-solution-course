

import pandas as pd
from sqlalchemy import create_engine

### Inserting data to the SQL database
df = pd.read_csv("../data/avocado.csv", index_col=0)
df.shape
df.head()

# some small data adjustments
df["Date"] = pd.to_datetime(df["Date"], infer_datetime_format=True).dt.strftime('%Y%m%d')
column_name_replacements = {"Total Volume":"TotalVolume",
                            "Total Bags": "TotalBags",
                            "Small Bags": "SmallBags",
                            "Large Bags": "LargeBags",
                            "XLarge Bags": "XLargeBags"}
df.rename(column_name_replacements, axis=1, inplace=True)
df.head()


# Load the data into our sql table
# reminder: dont store your credentials like this, this is only for illustrative purpose
connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format("root", "MyP4ssword123!", "34.65.173.67", "3306", "webapp_data")
engine = create_engine(connect_string)
df.to_sql("avocados", engine)

# Lets include the index
df.to_sql("avocados", engine, index=True)

# if the table already exists we have to specify what to do with the if_exists
# command. Options are 'replace' and 'append'
df.to_sql("avocados", engine, index=True, if_exists="replace")
# lets omit the index for now
df.to_sql("avocados", engine, index=False, if_exists="replace")

### reading data from the SQL database
# reading an entire dataset from sql
df_from_cloud = pd.read_sql("avocados", engine)
df_from_cloud.head()

# but we can also just run queries to receive data
# if a table has a column name with two words split by a space we can use the
# backtick symbols '`' to query that column. Be careful to not confuse the
# backticks with regular apostrophes
sql_query = "select Date, AveragePrice, `Total Volume`, region from avocados;"
df_from_cloud_subset = pd.read_sql_query(sql_query, engine)
df_from_cloud_subset.tail()


# adding a new row
row_values = {"AveragePrice": 2.70, "Total Volume": "100", "region": "Zurich"}
df_new_row = pd.DataFrame(row_values, index=[1])
df_new_row.to_sql("avocados",if_exists="append", con=engine, index=False)

### Using raw sql execution
# However, pandas is not made to be a one-stop-shop solution for database
# management. For this you will mostly have to use regular sql queries


### changing a value in a table
sql = "select * from avocados limit 3"
result = engine.execute(sql)
result.fetchall()



# sql query to update a row
sql_update_query = "UPDATE avocados SET Date = '2019-11-04' WHERE region = 'Zurich';"
engine.execute(sql_update_query)

# but this is unsafe due to the possibility of a sql injection
# SQL injection is a code injection technique that might destroy your database
# and that is one of the most common web hacking techniques.
# read more about it here: https://www.w3schools.com/sql/sql_injection.asp
sql = "UPDATE avocados SET `Total Volume` = %s WHERE region = %s;"
values = (200, "Zurich")
engine.execute(sql, values)


# deleting a row from a table
# the procedure is similar
sql = "DELETE FROM avocados WHERE AveragePrice > %s;"
values = (2.0)
r =engine.execute(sql, values)
# how many rows did we delete?
r.rowcount
# you can explore the response object with the dir() function
dir(r)


"""
*** Your turn: ***
Complete following exercises using the wine dataset

1. Load the data into your sql table
2. Create a new table in the sql that is a subset of the full wine dataset
    but only contains three four (preferably the ones that you used for
    your assignment) and the quality column.
3. Write a function that takes the four features as input parameters and adds
    these to the table as a new row, the wine quality value should be 'None'
    for now.
4. Add a form to your flask app that allows the user to enter the features and
    that adds this data to the sql table on submission, using your function
5. Use your linear regression model created in the first assignment and use it
    to predict the quality of the wine. Display that to the user in a separate
    field on the screen
6. Update your application running on App Engine with the new route and a new
    field in the navigation bar.
"""
