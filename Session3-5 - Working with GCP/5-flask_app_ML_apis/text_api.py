"""
1. Enable the cloud language API in your cloud console
2. Install the python packages: pip install google-cloud-language
3. Create new credentials for your application if you have not done so already
    https://console.cloud.google.com/apis/credentials
"""

from google.cloud import language
from google.cloud.language import types, enums
import os


# You are going to have to exchange this path for your credentials
# WARNING: when deploying to Google App Engine you can comment out this line as
# Google App engine automatically has the credentials to call the API contained
# in its environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/dominiquepaul/Google Drive/DSCS/dscs-unisg-6bdaad1e2ab3.json"

def language_analysis(text):
    # invokes the instance through which we can communicate with Google's server
    client = language.LanguageServiceClient()
    # As an input to the API we need to format our input text as a special document type.
    # This document contains further information which tells the API how to read it.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Run the sentiment analysis. This tells us what overall emotion of the
    # text is (good or bad) and how strong it is (0 to infinity)
    sent_analysis = client.analyze_sentiment(document)
    sentiment = sent_analysis.document_sentiment

    # When analysing for entities, the API will look at the specific words in
    # the text and try to identify their meaning in the text
    ent_analysis = client.analyze_entities(document)
    entities = ent_analysis.entities

    return(sentiment, entities)


sample1 = "Angela Merkel's party, the CDU, performed very poorly in this years german elections"
sentiment, entities = language_analysis(sample1)

sample2 = "What an incredible game, I really wasnt sure whether South Africa would be able to beat England"
sentiment, entities = language_analysis(sample2)

sample3 = "What an incredible game"
sentiment, entities = language_analysis(sample3)

sample4 = "The performance of the actor was truly atrocious!"
sentiment, entities = language_analysis(sample4)
