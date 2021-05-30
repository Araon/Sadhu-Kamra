
import tweepy
import sys
import json

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    alltweets = []  

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    print("Getting initial set of tweets")
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        print(f"Checkpoint: {oldest}")
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        #print(alltweets)
        print(f"{len(alltweets)} tweets downloaded")
        if len(alltweets) == 2990:
            break
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.text] for tweet in alltweets]
    print("Writing to csv file\n")
    with open(f'new_{screen_name}_tweets.json', 'w') as f:
        json.dump(outtweets, f)
    print(f'file:new_{screen_name}_tweets.json')
    pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets(sys.argv[1])