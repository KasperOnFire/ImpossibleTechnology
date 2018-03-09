import pandas as pd
import matplotlib as plt
import numpy as np
import webget

data_set_url = "https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv"
file_name = webget.download(data_set_url)

f18pdf = pd.read_csv(file_name)
f18pmatrix = f18pdf.as_matrix()

