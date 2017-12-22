import tweepy
from textblob import TextBlob


consumer_key = "oBAU4g0oK3UmunK01O6WpmAVP"
consumer_secret = "XRwdJr1Tskp1ifLtq6dOiR3uIsSocBRqWroO8IZICGsS0eqSyQ"

access_token = "278587203-dlQ0ZuLwJJa9ycqyve58vY5X7bpj56svtc6LLENi"
access_token_secret = "8NvAoPVE0rTdWSr6o8DCdHsNmNodwNEYFj5RuVTJepBrM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
