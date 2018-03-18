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
imdb_titles_matrix = imdb_titles.as_matrix()

# 0 tconst	1 titleType	2 primaryTitle	3 originalTitle	4 isAdult	5 startYear	6 endYear	7 runtimeMinutes	8 genres

def fileopener(path_to_file):
    with open(path_to_file) as f:
        for line in f:
            yield line

def question1():
    imdb_titles_movies = imdb_titles_matrix[imdb_titles_matrix[:, 1] != "movie"][:,5]
    imdb_titles_movies = imdb_titles_movies[imdb_titles_movies != "\\N"]
    
    years, count = np.unique(imdb_titles_movies.astype(int), return_counts=True)
    limit = 10

    years = years[np.argsort(-count)][:limit]
    count = np.sort(count)[::-1][:limit]

    plt.figure("Question 1")
    plt.title("Which year was the most movies released?")
    plt.xlabel("Years", fontSize=8)
    plt.ylabel("Count", fontSize=12)
    plt.bar(years, count)
    plt.xticks(np.arange(min(years), max(years) + 1, 1.0))
    plt.xticks(rotation=70)
    plt.tight_layout()
    for a, b in zip(years, count):
        plt.text(a, b, str(b), horizontalAlignment="center")
    plt.show()
    print("Question 1:\nMost movies where released in 2016 - see image for more details")

def question2():
    imdb_titles_series = imdb_titles[imdb_titles.endYear != "\\N"]
    series_endyear_count = imdb_titles_series.groupby("endYear")["endYear"].count()
    limit = 10
    years_with_most_ended_series = series_endyear_count.nlargest(limit)
    axes = years_with_most_ended_series.plot.bar()
    for p in axes.patches:
        axes.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.title("Which year did the most series end?")
    plt.xlabel("Years", fontSize=12)
    plt.xticks(rotation=90)
    plt.ylabel("Count", fontSize=12)
    plt.subplots_adjust(bottom=0.2)
    plt.show()
    print("Question 2:\nThe most series ended in 2017 - see image for more details")

    
def question3():
    movies = imdb_titles.loc[imdb_titles["titleType"] == "movie"]
    movies = movies[movies.genres != "\\N"]
    movies = movies[movies.runtimeMinutes != "\\N"]
    movies.runtimeMinutes = pd.to_numeric(movies["runtimeMinutes"], errors="coerce")
    movies_genre_count = movies.groupby("genres")["genres"].count()
    movies_genre_runtime_sum = movies.groupby("genres")["runtimeMinutes"].sum()
    movies_avg_runtime_by_genre = movies_genre_runtime_sum/movies_genre_count
    limit = 10
    longest_avg_runtime_by_genre = movies_avg_runtime_by_genre.nlargest(limit)
    
    plt.rc("font", size=10)
    ax = longest_avg_runtime_by_genre.plot.bar()
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.title("Genres with longest average runtime")
    plt.xlabel("Genre", fontSize=12)
    plt.xticks(rotation=90)
    plt.ylabel("Runtime(Minutes)", fontSize=12)
    plt.subplots_adjust(bottom=0.4)
    plt.show()
    print("Question 3 - longest average runtime per genre:")
    print(longest_avg_runtime_by_genre)

def question4_helper(genres, titletype):
    genre_dict = {}
    index = 0
    print('Running, can be a bit slow... So please dont worry!')
    for genre in genres:
        if titletype[index] == 'movie':
            genre_array = genre.split(',')
            for splitgenre in genre_array:
                if splitgenre != "\\N":
                    if splitgenre in genre_dict:
                        genre_dict[splitgenre] = genre_dict[splitgenre] + 1
                    else:
                        genre_dict[splitgenre] = 1
        index += 1
    return genre_dict
 
def question4():
    genres = imdb_titles.genres
    title_type = imdb_titles.titleType
    result = question4_helper(genres, title_type)

    lists = sorted(result.items())
    x, y = zip(*lists)
    
    plt.title("Which genre covers the most movies?")
    plt.xlabel("Genres", fontSize=12)
    plt.xticks(rotation=90)
    plt.ylabel("Amount", fontSize=12)
    plt.bar(x, y)
    plt.show()
    print("Question 4:\nThere are most drama movies in the dataset")
    print(result)

def question5():
    imdb_titles_adult = imdb_titles_matrix[imdb_titles_matrix[:, 4] == 1]
    imdb_titles_adult = imdb_titles_adult[imdb_titles_adult[:, 7] != "\\N"]
    average_runtime = np.asarray(imdb_titles_adult[:, 7].astype(int)).mean()
    print("Question 5:\nAverage runtime on adult films: %.2f minutes" % average_runtime)
    
question1()
question2()
question3()
question4()
question5()


