import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg
import gzip

file_link = "https://datasets.imdbws.com/title.basics.tsv.gz"
file_name = "imdb_titles.tsv"
zipped_file = wg.download(file_link, file_name)
file = gzip.GzipFile(zipped_file)
imdb_titles = pd.read_csv(file, delimiter='\t')
imdb_titles_matrix = imdb_titles.as_matrix()

print(imdb_titles)