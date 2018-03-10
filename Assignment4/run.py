import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg

file_link = "https://www.kaggle.com/kevinmh/fifa-18-more-complete-player-dataset/downloads/complete.csv/5"
file_name = "fifaplayers.csv"
#wg.download(file_link, "fifatest.csv")
FifaPlayers = pd.read_csv(file_name)
fp = FifaPlayers.as_matrix()


def question2():
    #get nationalities and count of each
    nationalities, count = np.unique(fp[:, 14], return_counts=True)
    #get only top 15
    limit = 15

    #sort both lists, in descending order for highest first
    nationalities = nationalities[np.argsort(-count)][:limit]
    count = np.sort(count)[::-1][:limit]

    #plot it
    plt.figure("Question 2")
    plt.title("Which nationality is the most common amongst all players?")
    plt.xlabel("Nationality", fontSize=8)
    plt.ylabel("Count", fontSize=12)
    plt.bar(nationalities, count)
    plt.xticks(rotation=70)
    plt.tight_layout()
    for a, b in zip(nationalities, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


def question3():
    players = []
    diff = []
    limit = 20
    for player in fp:
        players.append(player[1])
        diff.append(player[18] - player[17])

    players = players[np.argsort(-diff)][:limit]
    diff = np.sort(diff)[::-1][:limit]

    plt.figure("Question 3")
    plt.title(
        "What is the difference of the release clause and value of all players?"
    )
    plt.xlabel("Player", fontSize=8)
    plt.ylabel("Difference", fontSize=12)
    plt.bar(players, diff)
    plt.xticks(rotation=70)
    plt.tight_layout()
    for a, b in zip(players, diff):
        plt.text(a, b, str(b), horizontalAlignment="center")


question2()
question3()

plt.show()