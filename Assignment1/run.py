import xlrd
import matplotlib.pyplot as plt
import numpy as np


file_names = ["table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls",
"Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2013.xls"]

wb1 = xlrd.open_workbook(file_names[0]).sheet_by_index(0)

wb2 = xlrd.open_workbook(file_names[1]).sheet_by_index(0)

def question1():
    # Two different ways to get the years ou tif it wasn't for the bad data in the xls
    # years = [wb1.cell(el + 4, 0).value for el in range(20)]
    # y = wb1.col(0)[4:23]
    years = [year for year in range(1994, 2014)]
    total_crime = [
        wb1.cell(row, 2).value + wb1.cell(row, 12).value 
        for row in range(4, 24)]

    plt.figure('Question 1')                                    # Naming the window
    plt.title('Total crime', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Amount', fontsize=12)
    plt.grid(True)                                              # placing a grid to make it easier to read values
    plt.xticks(np.arange(min(years), max(years) + 1, 1.0))      # Control the interval of the ticks on the x axis
    plt.xticks(rotation=90)                                     # Rotating the years to make it more readable
    plt.bar(years, total_crime)                                 # inserting data


def question2():
    years = [year for year in range(1994, 2014)]
    
    crime_types = [
        wb1.cell(3, col).value for col in range(3, 20)]         # Getting the labels for all the different crimes
    
    crimes = []
    for col in range(3, 20):                                    # Getting the data for the different crimes
        crimes.append([wb1.cell(row, col).value for row in range(4, 24)]) 

    plt.figure("Question 2")                                    # Naming a new figure/window to give the graph a new window
    
    bars = []                                                   # keeping reference to asosiate info later in plt.legend
    for crime in crimes[1::2]:                                  # Insert every 2nd into the figure (don't need both numbers and rate)
        bars.append(plt.bar(years, crime))  # !!!!!! maybe rate is better to normalize due to an increase in population and should have ar bottom= to show the crime as an accumilated bar
    
    plt.legend((bar[0] for bar in bars), (crime_types))         # Placing the info about what color represent which crime
    plt.title('Crime', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Amount', fontsize=12)
    plt.grid(True)
    plt.xticks(np.arange(min(years), max(years) + 1, 1.0))
    plt.xticks(rotation=90)

def infoCollection(column):
    last_State = ''
    numberPerState = {}
    for i in range(4, 9296):
        if wb2.cell(i, 0).value != "":
            last_State = wb2.cell(i,0).value
            numberPerState[last_State] = 0
        if wb2.cell(i, column).value == "":
            numberPerState[last_State] = numberPerState[last_State] + 0
        else:
            numberPerState[last_State] =+ numberPerState[last_State] + int(wb2.cell(i, column).value)

    return numberPerState

def listofState():
    states = []
    for i in range(4, 9296):
        if wb2.cell(i, 0).value != "":
            states.append(wb2.cell(i, 0).value)
    
    return states

def question4():
    states = listofState()
    citizenPerState = infoCollection(2)
    violent_type = infoCollection(3)
    property_type = infoCollection(9)

    vperthousand = [] #violent type per thousand
    pperthousand = [] #property type per thousand

    for state in states:
        vperthousand.append((violent_type[state] / citizenPerState[state]) * 1000)
        pperthousand.append((property_type[state] / citizenPerState[state]) * 1000)
    print(vperthousand)
    print(pperthousand)

    plt.figure("Question 4")

# Using functions give a bit more of an overview and disable the ones you are not working on
question1()
question2()
question4()
plt.show()