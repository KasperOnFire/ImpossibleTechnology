import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_name = "KoreanConflict.csv"
KoreanConflict = pd.read_csv(file_name)
KoreanConflict = KoreanConflict.replace(np.nan,'',regex=True)
kc = KoreanConflict.as_matrix()


def question1():
    # Get unique branches, and the count of every branch
    branches, count = np.unique(kc[:, 3], return_counts=True)
    # and plot it!
    plt.figure("Question 1")
    plt.title(
        "How many soldiers entered from a marine corps branch?", fontSize=12)
    plt.xlabel("Branch", fontSize=12)
    plt.ylabel("Count", fontSize=12)
    plt.bar(branches, count)
    for a, b in zip(branches, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


#comments
def question2():
    enrollment, count = np.unique(kc[:, 2], return_counts=True)
    # and plot it!
    plt.figure("Question 2")
    plt.title("Which enrollment was the most common?", fontSize=12)
    plt.xlabel("Enrollment", fontSize=12)
    plt.ylabel("Count", fontSize=12)
    plt.bar(enrollment, count)
    for a, b in zip(enrollment, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


def question3():
    # fuckin errors, i DUNNO
    ethnicity, count = np.unique(kc[:, 15], return_counts=True)
    for i in range(len(ethnicity)):
        temp = ethnicity[i] 
        temp = temp.split('(')[0] 
        temp = temp.split('/')[0] 
        temp = temp.split('OR')[0] 
        temp = temp.replace(' ','\n')
        ethnicity[i] = temp
    # and plot it!
    plt.figure("Question 3")
    plt.title(
        "Was there an ethnicity majority throughout the war?", fontSize=12)
    plt.xlabel("Ethnicity", fontSize=12)
    plt.ylabel("Losses", fontSize=12)
    plt.bar(ethnicity, count)
    for a, b in zip(ethnicity, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


def question4():
    division, count = np.unique(kc[:, 18], return_counts=True)

    plt.figure("Question 4")
    plt.title("Which division had the most casualties?", fontSize=12)
    plt.xlabel("Division", fontSize=12)
    plt.ylabel("Losses", fontSize=12)
    plt.bar(division, count)
    for a, b in zip(division, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


def question5():
    mask = (kc[:, 11] == "US")
    us_soldiers = kc[mask]
    state, count = np.unique(us_soldiers[:, 13], return_counts=True)
    plt.figure("Question 5")
    plt.title("Which Home state suffered the most losses?", fontSize=12)
    plt.xlabel("State", fontSize=12)
    plt.ylabel("Losses", fontSize=12)
    plt.xticks(rotation=90)
    plt.bar(state, count)
    for a, b in zip(state, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


# run every highorder function
question1()
question2()
question3()
question4()
question5()

plt.show()