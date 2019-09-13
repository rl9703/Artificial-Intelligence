'''
    Author: Rishab Lalwani
    Title: Importing subreddits into json files
'''

import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='----', client_secret="---",
                     password='----', user_agent='----',
                     username='----')

#Import json files using pandas
subreddit1 = reddit.subreddit('chinese')
subreddit2 = reddit.subreddit('gameofthrones')
subreddit3 = reddit.subreddit('yoga')

#Create dictionary
topics_dict = { "title":[],
                "dataset":'chinese',
                'created':[],
                "body":[]}

# Concatenate top 500 posts from subreddit 1
for comment in subreddit1.top(limit=500):
    if not comment.stickied:
        topics_dict["title"].append(comment.title)
        topics_dict["created"].append(comment.created)
        topics_dict["body"].append(comment.selftext)


topics_data = pd.DataFrame(topics_dict)
#print(topics_data)
topics_data.to_json('subreddit1.json',orient='split')

topics_dict = { "title":[],
                "dataset":'gameofthrones',
                'created':[],
                "body":[]}

# Concatenate top 500 posts from subreddit 2
for comment in subreddit2.top(limit=500):
    topics_dict["title"].append(comment.title)
    topics_dict["created"].append(comment.created)
    topics_dict["body"].append(comment.selftext)

topics_data = pd.DataFrame(topics_dict)
#print(topics_data)
topics_data.to_json('subreddit2.json',orient='split')

topics_dict = { "title":[],
                "dataset":'yoga',
                'created':[],
                "body":[]}

# Concatenate top 500 posts from subreddit 3
for comment in subreddit3.top(limit=500):
    topics_dict["title"].append(comment.title)
    topics_dict["created"].append(comment.created)
    topics_dict["body"].append(comment.selftext)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_json('subreddit3.json',orient='split')


