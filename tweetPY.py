import tweepy
import time
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#insert your Twitter keys here
consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = '3XXXXXXXX'
access_secret ='XXXXXXXX'

twitter_handle = 'christinezhang' # replace with username you want

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

f = csv.writer(open('followers_python.csv', 'wb'))

f.writerow(["screenName", "name", "location", "description"])

users = tweepy.Cursor(api.followers, screen_name=twitter_handle, count = 200).items()

for u in users:
    screenName = u.screen_name
    name = u.name
    location = u.location

    f.writerow([screenName, name, location])

