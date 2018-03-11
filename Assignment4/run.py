import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg
from collections import OrderedDict
import operator #used to sort our dictonary!

file_link = "https://www.kaggle.com/kevinmh/fifa-18-more-complete-player-dataset/downloads/complete.csv/5"
file_name = "complete.csv"
#file_name = "fifaplayers.csv"
#wg.download(file_link, "fifaplayers.csv")
FifaPlayers = pd.read_csv(file_name)
fp = FifaPlayers.as_matrix()

def question1_dict_builder(club_list, value_list):
    clubsDict = {}
    index = 0
    for i in club_list:
        if i in clubsDict:
            clubsDict[i] = clubsDict[i] + value_list[index]
            index = index + 1
        else:
            clubsDict[i] = value_list[index]
            index = index + 1
    return clubsDict

def question1():
    df = pd.read_csv(file_name)

    result = question1_dict_builder(df.club, df.eur_value)
    result = OrderedDict(sorted(result.items(), key=operator.itemgetter(1)))
    result_list = list(result.keys())
    
    print('3 most expensive clubs: ', result_list[-3:])
    print('3 cheapest clubs: ', result_list[1:4])

    

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
    plt.show()

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

def question4():
    np.set_printoptions(suppress=True)
    player_ages, age_count = np.unique(fp[:, 6], return_counts = True)
    player_heights_cm, height_count = np.unique(fp[:, 9], return_counts = True)
    player_weights_kg, weight_count = np.unique(fp[:, 10], return_counts = True)
    player_count = fp.shape[0]
    age_frequence = np.around((age_count/player_count)*100, 3)
    height_frequence = np.around((height_count/player_count)*100, 3)
    weight_frequence = np.around((weight_count/player_count)*100, 3)

    title = "Age Frequence"
    plt.bar(player_ages, age_frequence, width=0.4, linewidth = 0, align = 'center')
    plt.title(title, fontsize = 18)
    plt.xticks(player_ages, player_ages)
    plt.xlabel("Age")
    plt.ylabel("%", fontsize = 18)
    plt.show()

    title = "Height Frequence"
    plt.bar(player_heights_cm, height_frequence, width=0.4, linewidth = 0, align = 'center')
    plt.title(title, fontsize = 18)
    plt.xticks(player_heights_cm, player_heights_cm, rotation="vertical")
    plt.xlabel("Height (cm)")
    plt.ylabel("%", fontsize = 18)
    plt.show()

    title = "Weight Frequence"
    plt.bar(player_weights_kg, weight_frequence, width=0.4, linewidth = 0, align = 'center')
    plt.title(title, fontsize = 18)
    plt.xticks(player_weights_kg, player_weights_kg, rotation="vertical")
    plt.xlabel("Weight (kg)")
    plt.ylabel("%", fontsize = 18)
    plt.show()



def question5():
    
    FifaPlayers["difference"] = FifaPlayers["eur_value"] - FifaPlayers["eur_wage"]
    player_count = fp.shape[0]
    print("The average difference between player wages and value:", str(round(FifaPlayers["difference"].sum()/player_count)), "EUR")


question1()
question2()
#question3()
question4()
question5()
plt.show()