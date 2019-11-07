import os
from google.cloud import language
from google.cloud.language import types, enums
# replace with your credentials path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/dominiquepaul/Google Drive/DSCS/dscs-unisg-5b8c0dcb7bf3.json"

# tweet from Donald Trump used as an example
text ="Our big Kentucky Rally on Monday night had a massive impact on all of the races. The increase in Governors race was at least 15 points, and maybe 20! Will be in Louisiana for @EddieRispone on Wednesday night. Big Rally!"


client = language.LanguageServiceClient()

document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

sent_analysis = client.analyze_sentiment(document)
sentiment = sent_analysis.document_sentiment

ent_analysis = client.analyze_entities(document)
entities = ent_analysis.entities

print(sentiment)
print(entities)
