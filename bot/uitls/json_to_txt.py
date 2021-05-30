import pandas as pd
df = pd.read_json (r'E:\Cody_stuff\Python stuff\Twitter_bot\Twitter_bot_template\bot\new_kunalkamra88_tweets.json')
df.to_csv (r'E:\Cody_stuff\Python stuff\Twitter_bot\Twitter_bot_template\bot\new_kunalkamra88_tweets_from_json.txt', index = False)