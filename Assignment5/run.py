import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg
import gzip

file_link = "https://datasets.imdbws.com/title.basics.tsv.gz"
file_name = "imdb_titles.tsv.gz"
zipped_file = wg.download(file_link, file_name)
file = gzip.GzipFile(zipped_file)
imdb_titles = pd.read_csv(file, delimiter='\t')
imdb_titles_matrix = imdb_titles.as_table()

# print(imdb_titles)
# 0 tconst	1 titleType	2 primaryTitle	3 originalTitle	4 isAdult	5 startYear	6 endYear	7 runtimeMinutes	8 genres


def question1():
    years, count = np.unique(imdb_titles_matrix[:, 5], return_counts=True)
    limit = 10

    years = years[np.argsort(-count)][:limit]
    count = np.sort(count)[::-1][:limit]

    plt.figure("Question 1")
    plt.title("Which year was the most movies released?")
    plt.xlabel("Years", fontSize=8)
    plt.ylabel("Count", fontSize=12)
    plt.bar(years, count)
    plt.xticks(rotation=70)
    plt.tight_layout()
    for a, b in zip(years, count):
        plt.text(a, b, str(b), horizontalAlignment="center")
   

question1()
plt.show()