import tweepy
from time import sleep
from credentials import keys
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print("Twitter bot which retweets,like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')

        # Follow the user who tweeted
        #check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')




        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
