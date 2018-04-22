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

    obama_tweet_16_count = obama_tweets_16.groupby([obama_tweets_16["created_at"].dt.week]).count()
    obama_tweet_17_count = obama_tweets_17.groupby([obama_tweets_17["created_at"].dt.week]).count()

    obama_16_bar = obama_tweet_16_count.plot(kind="bar", title="Obama tweet by week in 2016")
    obama_16_bar.set_xlabel("Weeks")
    obama_16_bar.set_ylabel("Amount of tweets")

    obama_17_bar = obama_tweet_17_count.plot(kind="bar", title="Obama tweet by week in 2017")
    obama_17_bar.set_xlabel("Weeks")
    obama_17_bar.set_ylabel("Amount of tweets")

    plt.show()
    print("Question 1")
    print("Obamas tweets per week in 2016 and 2017 can be seen in the two corresponding bar plots")

def question_2():
    trump_tweet_dates = trump_tweets_df[["created_at"]]
    
    trump_tweets_16 = trump_tweet_dates.where(trump_tweet_dates["created_at"].dt.year == 2016)
    trump_tweets_17 = trump_tweet_dates.where(trump_tweet_dates["created_at"].dt.year == 2017)
    trump_tweet_16_count = trump_tweets_16.groupby([trump_tweets_16["created_at"].dt.week]).count()
    trump_tweet_17_count = trump_tweets_17.groupby([trump_tweets_17["created_at"].dt.week]).count()
    
    
    trump_16_bar = trump_tweet_16_count.plot(kind="bar", title="Trump tweet by week in 2016")
    trump_16_bar.set_xlabel("Weeks")
    trump_16_bar.set_ylabel("Amount of tweets")

    trump_17_bar = trump_tweet_17_count.plot(kind="bar", title="Trump tweet by week in 2017")
    trump_17_bar.set_xlabel("Weeks")
    trump_17_bar.set_ylabel("Amount of tweets")
    
    plt.show()
    print("Question 2")
    print("Trump tweets per week in 2016 and 2017 can be seen in the two corresponding bar plots")

def question_3():
    slogan_count = count_containging(['yes we can', 'make america great again'], [obama_tweets_df.text, trump_tweets_df.text])
    plt.bar(['yes we can (Obama)', 'make america great again (Trump)'],slogan_count)
    plt.ylabel("Amount of tweets")
    plt.xlabel("Tweet subject")
    plt.show()
    print("Question 3")
    print("Obama wrote 'yes we can' 1 time in the data set")
    print("Trump wrote 'make america great again!' 62 times in the data set")


def question_4():
    iran_count = count_containging(['Iran','Iran'], [obama_tweets_df.text, trump_tweets_df.text])
    plt.bar(['Iran (Obama)','Iran (Trump)'], iran_count)
    plt.ylabel("Amount of tweets")
    plt.xlabel("Tweet subject")
    plt.show()
    print("Question 4")
    print("Obama wrote 'Iran' 61 time in the data set")
    print("Trump wrote 'Iran' 20 times in the data set")

def question_5():
    obamacare_count = count_containging(['Obamacare','Obamacare'], [obama_tweets_df.text, trump_tweets_df.text])
    plt.bar(['Obamacare (Obama)','Obamacare (Trump)'], obamacare_count)
    plt.ylabel("Amount of tweets")
    plt.xlabel("Tweet subject")
    plt.show()
    print("Question 5")
    print("Obama wrote 'Obamacare' 111 time in the data set")
    print("Trump wrote 'Obamacare' 109 times in the data set")

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

