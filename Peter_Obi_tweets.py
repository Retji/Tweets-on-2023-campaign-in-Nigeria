#!/usr/bin/env python
# coding: utf-8

# In[48]:


#importing the necessary libraries 

import pandas as pd
import snscrape.modules.twitter as sntwitter
import datetime
from csv import writer
import os

#Peter Obi tweets
po_tweets = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Peter Obi since:2022-10-17 until:2023-05-29').get_items()):
    if i>100:
        break
    po_tweets.append([tweet.date,tweet.user.username,tweet.user.displayname,tweet.content,tweet.likeCount,tweet.retweetCount,tweet.sourceLabel,tweet.user.followersCount,tweet.user.location])
    
# Creating a dataframe from the tweets list above 
po_tweets_data = pd.DataFrame(po_tweets, 
                         columns=["Date tweeted","username","display_name", "Tweets","Number_of_Likes","Number_retweets", "Source_of_Tweet","number_of_followers","location"])                                             


# In[31]:


po_tweets_data.to_csv("Po_tweets.csv",index=False)
#Exporting the stock_price_list to my local document folder as a csv file))

