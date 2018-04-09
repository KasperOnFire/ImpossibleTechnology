import csv
import pandas as pd
from collections import Counter


file_name = 'trades_march_to_april_2018.csv'
df = pd.read_csv(file_name, sep=';')

def question1():
    largest_trans = 0
    for row in df.sizetransfer:
        amount = float(row)
        if largest_trans < amount:
            largest_trans = amount
    print(largest_trans)

def question2():
    print('TBD')

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
    print(buy_sum / buy_trans)
    print(sell_sum / sell_trans)
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