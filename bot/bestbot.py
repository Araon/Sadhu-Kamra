import tweepy
import logging
from config import create_api
from dhook import notify

import random


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

api = create_api()

def tweet(message):
    try:
        api.update_status(status = message)
        logger.info("Tweet Posted!")
    except tweepy.TweepError as error:
        if error.api_code == 187:
            logger.error("Dublicate tweet!")
        else:
            logger.error("Error posting Tweet")

def get_tweet():
    with open("generate_tweets.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        tweet = lines[random.randint(0,len(lines))]
        logger.info(tweet)
        return tweet
    
def main():
    generate_tweet = get_tweet()
    tweet(generate_tweet)
    notify(generate_tweet)


if __name__ == "__main__":
   main()




