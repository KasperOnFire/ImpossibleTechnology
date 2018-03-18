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
#imdb_titles = imdb_titles[imdb_titles.runtimeMinutes != r"\N"]
#imdb_titles = imdb_titles.replace("\\n", '', regex=True)
imdb_titles_matrix = imdb_titles.as_matrix()

# print(imdb_titles)
# 0 tconst	1 titleType	2 primaryTitle	3 originalTitle	4 isAdult	5 startYear	6 endYear	7 runtimeMinutes	8 genres

def fileopener(path_to_file):
    with open(path_to_file) as f:
        for line in f:
            yield line

def question1():
    mask = (imdb_titles_matrix[:, 1] != "movie")
    imdb_titles_movies = imdb_titles_matrix[mask][:,5]
    imdb_titles_movies = imdb_titles_movies[imdb_titles_movies != "\\N"]
    
    years, count = np.unique(imdb_titles_movies.astype(int), return_counts=True)
    limit = 10

    years = years[np.argsort(-count)][:limit]
    count = np.sort(count)[::-1][:limit]

    plt.figure("Question 1")
    plt.title("Which year was the most movies relea sed?")
    plt.xlabel("Years", fontSize=8)
    plt.ylabel("Count", fontSize=12)
    plt.bar(years, count)
    plt.xticks(np.arange(min(years), max(years) + 1, 1.0))
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
    movies = imdb_titles.loc[imdb_titles["titleType"] == "movie"]
    movies = movies[movies.genres != "\\N"]
    movies = movies[movies.runtimeMinutes != "\\N"]
    #movie_genres = tuple(movies.genres.unique())
    #print(movie_genres)
    movies_by_genre = np.asarray(movies.groupby("genres").get_group("Western")["runtimeMinutes"]).astype(int).mean()
    answer = "Average runtime for westerns: %f minutes" %(movies_by_genre)
    print(answer)

def question4():
    pass

def question5():
    mask = (imdb_titles_matrix[:, 4] == 1)
    imdb_titles_adult = imdb_titles_matrix[mask]
    imdb_titles_adult = imdb_titles_adult[imdb_titles_adult[:, 7] != "\\N"]
    adult_movies_count = imdb_titles_adult.shape[0]
    average_runtime = np.sum(imdb_titles_adult[:, 7].astype(int)) / adult_movies_count
    print(average_runtime)

<<<<<<< HEAD
<<<<<<< HEAD
#question1()
#question2()
question3()
#question5()
=======
question1()
# question2()
# question5()
>>>>>>> 10e1f30a4d320430891070c29451dd9e3d83764d
=======
# question1()
# question2()
question5()
>>>>>>> 0429f49c1a1d9ae157d29efda69d245c5018c1bb
