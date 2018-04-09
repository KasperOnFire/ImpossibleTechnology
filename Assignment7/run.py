import csv
import pandas as pd


file_name = 'trades_march_to_april_2018.csv'
df = pd.read_csv(file_name, sep=';')

def question1():
    largest_trans = 0
    for row in df.sizetransfer:
        amount = float(row)
        if largest_trans < amount:
            largest_trans = amount
    print(largest_trans)

''' def question2():
    with open(file_name, encoding='utf-8') as f: '''

question1()