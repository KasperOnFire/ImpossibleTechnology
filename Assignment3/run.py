import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_name = "KoreanConflict.csv"
KoreanConflict = pd.read_csv(file_name)
kc = KoreanConflict.as_matrix()


def question1():
    # Get unique branches, and the count of every branch
    branches, count = np.unique(kc[:, 3], return_counts=True)

    # and plot it!
    plt.figure("Question 1")
    plt.title(
        "How many soldiers entered from a marine corps branch?", fontSize=12)
    plt.xlabel("branch", fontSize=12)
    plt.ylabel("count", fontSize=12)
    plt.bar(branches, count)
    for a, b in zip(branches, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


def question2():
    enrollment, count = np.unique(kc[:, 2], return_counts=True)

    # and plot it!
    plt.figure("Question 2")
    plt.title("Which enrollment was the most common?", fontSize=12)
    plt.xlabel("Enrollment", fontSize=12)
    plt.ylabel("count", fontSize=12)
    plt.bar(enrollment, count)
    for a, b in zip(enrollment, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


def question3():
    # fuckin errors, i DUNNO
    #ethnicity, count = np.unique(kc[:, 15], return_counts=True)
    # and plot it!
    plt.figure("Question 3")
    plt.title(
        "Was there an ethnicity majority throughout the war - If so, which?",
        fontSize=12)
    plt.xlabel("ethnicity", fontSize=12)
    plt.ylabel("count", fontSize=12)
    plt.bar(ethnicity, count)
    for a, b in zip(ethnicity, count):
        plt.text(a, b, str(b), horizontalAlignment="center")


# run every highorder function
question1()
question2()
#question3()

plt.show()