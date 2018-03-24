#coding = utf-8

import re
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "RNOGX5TiB0Kyto9ggDxcT8Gie"
consumer_secret = "Kn7ut4mvlwqPDNXIrl9uQxAblb1115Rg87XZ319UEaaJ09Kf0i"
access_token = "3293164734-flLNI737Kx80gPEsJN5DBMXHN2uCew8HYkSwsQD"
access_token_secret = "uMktnXidYlONSa3lV45AXPS7mvnW5k0YAU7wwWTPqDFrB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
result = []

# nameArray = ["kilicdarogluk","erenerdemnet"]
nameArray = []
tweetCount = 9999999

#url of query
def urlQuery(url):
    return len(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)) or len(re.findall('RT|@|#+', url))
#base function
def get_tweet(name,tweetCount) :
    i = 1
    for tweet in tweepy.Cursor(api.user_timeline,id=name).items(tweetCount):
        if urlQuery(tweet.text) < 1 :
            urlQuery(tweet.text)
            result.append({i: {
                'text': tweet.text.strip("https…"),
                'author_name': tweet.user.screen_name
            }})
            i = i + 1
    i=1
    with open('data/'+name+'.json', 'w+', encoding='utf-8') as file:
        json.dump(result, file,ensure_ascii=False)



with open("users.json", encoding='utf-8') as users:
    users = json.load(users)
    for user in users:
        nameArray.append(user["name"])

#get and writer tweets...

for name in nameArray :
    get_tweet(name,tweetCount)
    result = []