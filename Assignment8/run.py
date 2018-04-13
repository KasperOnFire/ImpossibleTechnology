import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import webget as wg

file_link = "https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv"
file_name = "kickstarter_projects.csv"
wg.download(file_link, file_name)
ks_df = pd.read_csv(file_name)
ks_matrix = ks_df.as_matrix()

# matrix column numbers:
# 0 = ID | 1 = name | 2 = category| 3 = main_category | 4 = currency | 5 = deadline
# 6 = goal | 7 = launched | 8 = pledged | 9 = state | 10 = backers | 11 = country
# 12 = usd pledged | 13 = usd_pledged_real | 14 = usd_goal_real

def question_1():
    main, count = np.unique(ks_matrix[:, 3], return_counts=True)
    main = main[np.argsort(-count)]
    count = np.sort(count)[::-1]

    mask = (ks_matrix[:, 9] == "successful")
    successful_ks_projects = ks_matrix[mask]
    main_success, success_count = np.unique(successful_ks_projects [:, 3], return_counts=True)
    main_success = main_success[np.argsort(-count)]
    success_count = np.sort(success_count)[::-1]

    success_rate = (success_count/count)*100

    plt.figure("Question 1")
    plt.title("Most sucessful kickstarter main category?")
    plt.xlabel("Main Category", fontSize=10)
    plt.ylabel("Success rate (%)", fontSize=12)
    plt.bar(main_success, success_rate)
    plt.xticks(rotation=70)
    plt.tight_layout()
    for a, b in zip(main_success, success_rate):
        plt.text(a, b, str(format(b, "0.2f")), horizontalAlignment="center")
    plt.show()

    print("Question 1")
    print("Journalism is the most successful main category with a 53.53% successrate")

def question_2():
    mask = (ks_matrix[:, 3] == "Journalism")
    journalism_ks_projects = ks_matrix[mask]
    category, count = np.unique(journalism_ks_projects[:, 2], return_counts=True)
    category = category[np.argsort(-count)]
    count = np.sort(count)[::-1]

    plt.figure("Question 2")
    plt.title("Most proposed project category for journalism?")
    plt.xlabel("Category", fontSize=10)
    plt.ylabel("Count", fontSize=12)
    plt.bar(category, count)
    plt.xticks(rotation=70)
    plt.tight_layout()
    for a, b in zip(category, count):
        plt.text(a, b, str(b), horizontalAlignment="center")
    plt.show()

    print("Question 2")
    print("Journalism is the proposed category with 1747 projects")

def question_3():
    mask = (ks_matrix[:, 9] == "successful")
    successful_ks_projects = ks_matrix[mask]
    ks_pledge_median = np.median(successful_ks_projects[:,12])
    result = "The pledged median of successful projects is: " + str(ks_pledge_median)
    print("Question 3")
    print(result)
    
question_1()
question_2()
question_3()