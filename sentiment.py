import rmp
from transformers import pipeline

#input must be valid json object from get_prof_info output
def get_sentiment(prof_json):
    sentiment_pipeline = pipeline('sentiment-analysis')
    for key in prof_json.keys():
        for comment in prof_json[key]['comments']:
            print(comment, sentiment_pipeline(comment))


get_sentiment(rmp.get_prof_info("1112", "Geoffrey Challen"))