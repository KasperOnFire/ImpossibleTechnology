import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg
import datetime as dt


obama_tweet_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/BarackObama.csv"
trump_tweet_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/realDonaldTrump.csv"
obama_tweet_csv = "Obama.csv"
trump_tweet_csv = "Trump.csv"
# wg.download(obama_tweet_url, obama_tweet_csv)
# wg.download(trump_tweet_url, trump_tweet_csv)

obama_tweets_df = pd.read_csv(obama_tweet_csv, sep=',', parse_dates=[0], encoding = "ISO-8859-1")
obama_tweets_matrix = obama_tweets_df.as_matrix()

trump_tweets_df = pd.read_csv(trump_tweet_csv, sep=',', parse_dates=[0], encoding = "ISO-8859-1")
trump_tweets_matrix = trump_tweets_df.as_matrix()

def question_1():
    obama_tweet_dates = obama_tweets_df[["created_at"]]

    obama_tweets_16 = obama_tweet_dates.where(obama_tweet_dates["created_at"].dt.year == 2016)
    obama_tweets_17 = obama_tweet_dates.where(obama_tweet_dates["created_at"].dt.year == 2017)

    obama_tweet_16_count = obama_tweets_16.groupby([obama_tweets_16["created_at"].dt.year, obama_tweets_16["created_at"].dt.week]).count()
    obama_tweet_17_count = obama_tweets_17.groupby([obama_tweets_17["created_at"].dt.year, obama_tweets_17["created_at"].dt.week]).count()
    
    print("Obamas tweets per week in 2016")
    print(obama_tweet_16_count)
    print("Obamas tweets per week in 2017")
    print(obama_tweet_17_count)

def question_2():
    trump_tweet_dates = trump_tweets_df[["created_at"]]
    
    trump_tweets_16 = trump_tweet_dates.where(trump_tweet_dates["created_at"].dt.year == 2016)
    trump_tweets_17 = trump_tweet_dates.where(trump_tweet_dates["created_at"].dt.year == 2017)
    trump_tweet_16_count = trump_tweets_16.groupby([trump_tweets_16["created_at"].dt.year, trump_tweets_16["created_at"].dt.week]).count()
    trump_tweet_17_count = trump_tweets_17.groupby([trump_tweets_17["created_at"].dt.year, trump_tweets_17["created_at"].dt.week]).count()
    
    print("Trump tweets per week in 2016")
    print(trump_tweet_16_count)
    print("Trump tweets per week in 2017")
    print(trump_tweet_17_count)

def question_3():
    print(count_containging(['yes we can', 'make america great again'], [obama_tweets_df.text, trump_tweets_df.text]))

def question_4():
    print(count_containging(['Iran','Iran'], [obama_tweets_df.text, trump_tweets_df.text]))

def question_5():
    print(count_containging(['Obamacare','Obamacare'], [obama_tweets_df.text, trump_tweets_df.text]))

def count_containging(substrings, arrays):
    counts = []
    for i in range(len(arrays)):
        counts.append(substring_count_in_array(substrings[i], arrays[i]))
    return counts


def substring_count_in_array(substring, array):
    count = 0
    for el in array:
        if substring.lower() in el.lower():
            count += 1
    return count


question_1()
question_2()
question_3()
question_4()
question_5()
