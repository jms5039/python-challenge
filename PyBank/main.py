# import the os module
import os

# Module for reading CSV files
import csv

# set path for file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    # reading data in dictionary form
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # making a list of dictionaries
    budget_data = list(csvreader)

    # storing date values in list. casting profit/losses to integer and storing values in list
    months = [row["Date"] for row in budget_data]
    profit_losses = [int(row["Profit/Losses"]) for row in budget_data]

    #initializing to zero
    total_months = 0

    # loop through dates and get total count
    for month in months :
        total_months = total_months+1

    # get total of values in profit/losses list
    net_profitLosses = sum(profit_losses)

    #loop through profit/losses list and get the difference between value and next value. Subtract 1 from length of list since loop is looking ahead one spot for equation
    profitLoss_change = [profit_losses[i+1]-profit_losses[i] for i in range(len(profit_losses)-1)]
    
    # total the values in profit/losses change list
    total_profitLoss_change = sum(profitLoss_change)

    #get the average change by dividing the total profit/losses change by the total number of values
    average_ProfitLoss_change = total_profitLoss_change/len(profitLoss_change)

    # Since I am going to join months list and profit/losses change list, value for first month needs to be added to profit/lossse change list in order for dates to match properly to correct values
    profitLoss_change.insert(0, 1088983)
   
   # build dictionary with dates and changes in profit/losses for each date
    months_profitLoss_change_dictionary = dict(zip(months, profitLoss_change))

    # find the smallest and largest values in the profit/losses change dictionary
    greatest_increase =max(months_profitLoss_change_dictionary.values())
    greatest_decrease = min(months_profitLoss_change_dictionary.values())
 
    # get a list of keys and a list of values for profit/losses change dictionary
    keys = list(months_profitLoss_change_dictionary.keys())  
    values = list(months_profitLoss_change_dictionary.values())  
      
    # Getting the index of the stored value from the list of values  
    index_increase = values.index(greatest_increase)  
    index_decrease = values.index(greatest_decrease)
      
    # Getting the key of the value  
    Key_increase = keys[index_increase]  
    Key_decrease = keys[index_decrease]

    # Specify the file to write to
    output_path = os.path.join("..", "PyBank", "analysis", "analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents. write the variable in file.
    lines = (f"Financial Analysis\n -----------------------------------------------\nTotal Months: {total_months}\nTotal: {net_profitLosses}\nAverage Change: {average_ProfitLoss_change}\nGreatest Increase in Profits: {Key_increase} {greatest_increase}\nGreatest Decrease in Profits: {Key_decrease} {greatest_decrease}")
    with open(output_path, 'w') as txtfile:
         txtfile.write(lines)

# print analysis to terminal
print("Financial Analysis")
print("------------------------------------------------------------------------------")
print("Total Months: ", total_months)
print("Total: ", net_profitLosses)
print("Average Change: ", average_ProfitLoss_change )
print("Greatest Increase in Profits: ", Key_increase, greatest_increase )
print("Greatest Decrease in Profits: ", Key_decrease, greatest_decrease)