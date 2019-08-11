from RealTimeTweetListener import  RealTimeTweetListener
from tweepy import OAuthHandler
from tweepy import Stream
import config

def return_tweets_by_tag(tweet_string=None):
    if tweet_string is not None:
        config_keys = get_config_keys()
        if len(config_keys.keys()) == 0:
            raise Exception("API Config Keys Not Present in config.py.")
        else:
            listener = RealTimeTweetListener()
            auth = OAuthHandler(config_keys['CONSUMER_API_KEY'], config_keys['COMSUMER_API_SECRET'])
            auth.set_access_token(config_keys['ACCESS_TOKEN'], config_keys['ACCESS_TOKEN_SECRET'])
            stream = Stream(auth, listener)
            stream.filter(track=[tweet_string])


def get_config_keys():
    config_keys = {}
    try:
        config_keys['CONSUMER_API_KEY']    = config.CONSUMER_API_KEY
        config_keys['COMSUMER_API_SECRET'] = config.COMSUMER_API_SECRET
        config_keys['ACCESS_TOKEN']        = config.ACCESS_TOKEN
        config_keys['ACCESS_TOKEN_SECRET'] = config.ACCESS_TOKEN_SECRET
    except Exception:
        raise Exception("Config Keys undefined.")
    return config_keys

def return_tweets_by_user():
    pass


def is_user(search_string=None):
    pass


def is_tag(search_string=None):
    pass


def find(tweet_string=None):
    pass

