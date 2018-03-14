from collections import Counter, OrderedDict
import pandas as pd
import operator

file_name = 'stackoverflow_survey_result.csv'
pd_file = pd.read_csv(file_name)

def question1(): #Missing plots
    result = Counter(pd_file.Professional)
    print(result)

def question2():
    pass

def question3(): #Missing plots
    result = {}
    language = pd_file.HaveWorkedLanguage
    for string in language:
        if type(string) == str:
            splitted = string.split(';')
            for split in splitted:
                split = split.replace(' ','') #Removing spaces since they give problems with same IDE having a space where it shouldnt be, creating duplications
                if split in result:
                    result[split] += 1
                else:
                    result[split] = 1
    print(result)

def question4(): #Missing plots
    result = {}
    ide = pd_file.IDE
    for string in ide:
        if type(string) == str:
            splitted = string.split(';')
            for split in splitted:
                split = split.replace(' ','') #Removing spaces since they give problems with same IDE having a space where it shouldnt be, creating duplications
                if split in result:
                    result[split] += 1
                else:
                    result[split] = 1
    print(result)

def question5(): #Done
    result = {}
    framework = pd_file.WantWorkFramework
    for string in framework:
        if type(string) == str:
            splitted = string.split(';')
            for split in splitted:
                split = split.replace(' ','') #Removing spaces since they give problems with same IDE having a space where it shouldnt be, creating duplications
                if split in result:
                    result[split] += 1
                else:
                    result[split] = 1
    sorted_result = OrderedDict(sorted(result.items(), key=operator.itemgetter(1)))
    abc = list(sorted_result.keys())
    print('Answer question 5:', abc[-1:])

question1()
question3()
question4()
question5()