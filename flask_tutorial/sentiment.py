import rmp_
from transformers import pipeline

#input must be valid json object from get_prof_info output
def get_sentiment(prof_json):
    sentiment_pipeline = pipeline('sentiment-analysis')
    for key in prof_json.keys():
        for comment in prof_json[key]['comments']:
            print(comment, sentiment_pipeline(comment))

a = rmp_.get_prof_info("1112", "Geoffrey Challen")
get_sentiment(rmp_.get_prof_info("1112", "Geoffrey Challen"))