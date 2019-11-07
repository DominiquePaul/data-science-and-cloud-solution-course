"""
1. Create an autoML project
2. Create new credentials or modify the permissions of a service account linked
    to credentials you already have. You can create new credentials at:
    https://console.cloud.google.com/apis/credentials
    Set the role as 'autoML predictor'
3. Install the auto ML python package by running
    pip install google-cloud-automl
"""

import os
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

# replace these with your path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/dominiquepaul/Google Drive/DSCS/auto_ml_auth.json"

# the path to the file we want to use
file_path = "./test_image.jpg"
# the Project ID: you can find this on the starting page of the GCP console
project_id = "1048264514027"
# You can find the model id in the 'Models' submenu of the autoML
model_id = "ICN6042515684024385536"

# reads in the file
with open(file_path, 'rb') as ff:
    content = ff.read()

# initiate the client
prediction_client = automl_v1beta1.PredictionServiceClient()

# create the connection string for making the prediction
name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
payload = {'image': {'image_bytes': content }}
params = {}
request = prediction_client.predict(name, payload, params)

# print the result
print(request)
