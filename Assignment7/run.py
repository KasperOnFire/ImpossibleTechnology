import csv
import pandas as pd
from collections import Counter

import matplotlib.pyplot as plt

import datetime as dt

file_name = 'info.csv'
df = pd.read_csv(file_name, sep=';')

def question1():
    largest_trans = 0
    for row in df.sizetransfer:
        amount = float(row)
        if largest_trans < amount:
            largest_trans = amount
    print('%.2f' % largest_trans)

def question2():
    time_df = pd.read_csv(file_name, sep=';', parse_dates=[1], index_col=[0])
    time_df2 = time_df[['time_exchange']]
    result = time_df2.groupby(time_df2["time_exchange"].dt.hour).count()
    result_bar = result["time_exchange"].plot.bar()
    result_bar.set_xlabel("Time(Hours) on 7/4 2018")
    result_bar.set_ylabel("Number of transactions")
    result_bar.set_title("Question 2")
    plt.show()
    print("The hours with the most transactions can be seen in the bar plot with the title 'Question 2' ")
def question3():
    result = Counter(df.taker_side)
    print(result)

def question4():
    price = df.price
    trans_type = df.taker_side
    index = 0
    buy_sum = 0
    buy_trans = 0
    sell_sum = 0
    sell_trans = 0
    for row in trans_type:
        index += 0
        if row == 'BUY':
            buy_sum += price[index]
            buy_trans += 1
        else:
            sell_sum += price[index]
            sell_trans += 1
    
    print('%.2f' % (buy_sum / buy_trans))
    print('%.2f' % (sell_sum / sell_trans))
    print('Seems odd the results are the same (basicly) but would make sense in the way that this is both sellings and buyings! And the one buying is buying from the one selling.')
    
def question5():
    print('TBD')

print('\nquestion 1')
question1()
print('\nquestion 2')
question2()
print('\nquestion 3')
question3()
print('\nquestion 4')
question4()
print('\nquestion 5')
question5()