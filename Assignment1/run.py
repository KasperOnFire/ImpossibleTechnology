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
    




# Using functions give a bit more of an overview and disable the ones you are not working on
question1()
question2()
plt.show()