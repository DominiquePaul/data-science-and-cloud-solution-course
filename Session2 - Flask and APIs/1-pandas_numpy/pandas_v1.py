"""
This script serves as a basic run-through of the numpy and flask package. Its
purpose is not to explain all of the essential functions of the two functions,
but rather to demonstrate briefly what is possible and give you a feel for what
you can do with these packages, so you know where to look for when you have an
idea

For more information on how pandas and numpy work check out this youtube series:
https://www.youtube.com/watch?v=Iqjy9UqKKuo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-

To run the script you might have to run the following commands in your terminal
first. If you have installed python with anaconda then replace 'pip' with 'conda'

pip install numpy
pip install pandas
pip install statsmodels
pip install seaborn
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns

# reading in a dataframe as csv
df = pd.read_csv("./data/wdbc_csv_dirty.csv", sep=",")

# selecting a single cell/value
df.iloc[1,4]

# selecting multiple rows and a column
df.loc[1:10,"mean_perimeter"]

# selecting multiple rows and several columns
df.loc[1:10,["mean_perimeter","mean_area", "Class"]]

# creating a subset of our original data
df_subset = df.iloc[:, [1,2,3,4,5,-1]]

# we split it into out training and test set
row_to_split_at = np.round(0.7 * len(df_subset), 0)

# split into training and testing data --> does not work
df_train = df_subset.iloc[:row_to_split_at, :]
df_test = df_subset.iloc[row_to_split_at:, :]

# the number we received is a float, but we need an integer, so we just repeat
# repeat the previous step and convert the number to an integer
type(row_to_split_at)
row_to_split_at = int(np.round(0.7 * len(df_subset), 0))

# repeat the splitting
df_train = df_subset.iloc[:row_to_split_at, :]
df_test = df_subset.iloc[row_to_split_at:, :]

# creating a logistic regression --> does not work
reg = sm.Logit(np.asarray(df_train.iloc[:,5]), np.asarray(df_train.iloc[:,0:5]))

# we cant run our regression because some of our values are empty
intermediate_output = df_train.isna().any(axis=1).sum()

# we can use this to create a 'mask' of our original dataframe
df_train[df_train.isna().any(axis=1)]
# but we want exactly the opposite!

# or defined the other way around
df_train.notna().product(axis=1)
# but we need booleans for our next step, so we just convert them
df_train.notna().product(axis=1).astype("bool")

# using this list of 'boolean' values we can select a 'mask' of our dataset
# we re-run this on the subset data to make sure we have the correct alignment
# of the decision features and the class labels
df_train = df_train.loc[df_train.notna().product(axis=1).astype("bool"), :]
df_test = df_test.loc[df_test.notna().product(axis=1).astype("bool"), :]

# For most of the problems that not only we but also others are likely to
# encounter, there are often pre-written functions in packages which make these
# things easier. In this case, we could for example use the dropna command of
# pandas.
# df_train = df_train.dropna()
# df_test = df_test.dropna()


# we repeat our regression --> does not work
reg = sm.Logit(np.asarray(df_train.iloc[:,5]), np.asarray(df_train.iloc[:,0:5]))
reg_fitted = reg.fit()
reg_fitted.summary()

# another problem! Our classification variables must be between 0 and 1, not 1
# and 2. We can quickly fix this though by subtracting 1 one from the entire
# column. Thanks to pandas, this is very easy to do for the entire column
df_train["Class"] = df_train["Class"] - 1
df_test["Class"] = df_test["Class"] - 1

# now finally our logistic regression works
reg = sm.Logit(np.asarray(df_train.iloc[:,5]), np.asarray(df_train.iloc[:,0:5]))
reg_fitted = reg.fit()
reg_fitted.summary()

# no we can use our model to make predictions
predictions = reg_fitted.predict(df_test.iloc[:,:5])
sns.scatterplot(df_test["mean_area"], predictions)

predictions = np.where(predictions >0.9, 1, 0)
df_test["predictions"] = predictions


# plot one of our graphs
sns.scatterplot(df_test["mean_area"], df_test["predictions"])


# we save our results for a potential review and analysis
df_test.to_csv("./saved_predictions.csv", sep=",")

# Say we are just interest in a single value, e.g. if making a prediction for
# just one user on our website. Then we can also feed in data like this
single_data_point = [21.02, 124.5, 993.0, 0.124, 0.25]
single_prediction = reg_fitted.predict(single_data_point)
# we are going to receive our single value returned as an array, so we have to
# 'unpack' it
single_prediction[0]
