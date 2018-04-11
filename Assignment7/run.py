import csv
import pandas as pd
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

file_name = 'info.csv'
df = pd.read_csv(file_name, sep=';')

font = {'family': 'normal', 'weight': 'bold', 'size': 16}

matplotlib.rc('font', **font)


def question1():
    max_transfer = np.max(df.sizetransfer)
    print('%.2f' % max_transfer)


def question2():
    time_df = pd.read_csv(file_name, sep=';', parse_dates=[1], index_col=[0])
    time_df2 = time_df[['time_exchange']]
    result = time_df2.groupby(time_df2["time_exchange"].dt.hour).count()
    result_bar = result["time_exchange"].plot.bar()
    result_bar.set_xlabel("Time(Hours) on 7/4 2018")
    result_bar.set_ylabel("Number of transactions")
    result_bar.set_title("Question 2")
    plt.tight_layout()
    plt.show()
    print(
        "The hours with the most transactions can be seen in the bar plot with the title 'Question 2' "
    )


def question3():
    result = Counter(df.taker_side)
    print(result)


def question4():
    prices = np.asarray(df)
    buy = prices[prices[:,6] == 'BUY'][:,4]
    sell = prices[prices[:,6] == 'SELL'][:,4]
    print('%.2f' % buy.mean())
    print('%.2f' % sell.mean())


def question5():
    # all transactions are from the same day in the data provided
    total = np.sum(df.sizetransfer)
    print('%.2f' % total)

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