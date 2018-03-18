import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg
import gzip

file_link = "https://datasets.imdbws.com/title.basics.tsv.gz"
file_name = "imdb_titles.tsv.gz"
zipped_file = wg.download(file_link, file_name)
file = gzip.GzipFile(zipped_file)
imdb_titles = pd.read_table(file)
imdb_titles = imdb_titles.replace("\\n", '', regex=True)
imdb_titles_matrix = imdb_titles.as_matrix()

# print(imdb_titles)
# 0 tconst	1 titleType	2 primaryTitle	3 originalTitle	4 isAdult	5 startYear	6 endYear	7 runtimeMinutes	8 genres


def question1():
    mask = (imdb_titles_matrix[:, 1] != "movie")
    imdb_titles_movies = imdb_titles_matrix[mask][:,5]
    imdb_titles_movies = imdb_titles_movies[imdb_titles_movies != "\\N"]
    imdb_titles_movies = np.array([str(x) for x in imdb_titles_movies])
    
    print(imdb_titles_movies)
    years, count = np.unique(imdb_titles_movies, return_counts=True)
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
    plt.show()

def question2():
    imdb_titles_series = imdb_titles[imdb_titles.endYear != "\\N"]
    series_endyear_count = imdb_titles_series.groupby("endYear")["endYear"].count()
    limit = 10
    years_with_most_ended_series = series_endyear_count.nlargest(limit)
    years_with_most_ended_series.plot.bar()
    plt.title("Which year did the most series end?")
    plt.xlabel("Years", fontSize=12)
    plt.xticks(rotation=90)
    plt.ylabel("Count", fontSize=12)
    plt.subplots_adjust(bottom=0.2)
    plt.show()
    
def question3():
    pass

def question4():
    pass

def question5():
    mask = (imdb_titles_matrix[:, 4] == 1)
    imdb_titles_adult = imdb_titles_matrix[mask]
    adult_movies_count = imdb_titles_adult.shape[0]
    average_runtime = imdb_titles_adult[:, 7].astype(int) / adult_movies_count
    print(average_runtime)

question1()
# question2()
# question5()
