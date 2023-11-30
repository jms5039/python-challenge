import os
import csv
# total_months = 
# net_total_amount_Profit_Losses =
# changes_Profit_Losses =
# average_changes_Profit_Losses =
# greatest_increase_profits_date = 
# greatest_increase_profits_amount = 
# greatest_decrease_profits_date =
# greatest_decrease_profits_amount =

# print("Financial Analysis")

# print("----------------------------------------------------------------------")

# print("Total Months: ")
# print("Total: ")
# print("Average Change: ")
# print("Greatest Increase in Profits: ")
# print("Greatest Decrease in Profits: ")

budget_data_csv = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')

# Lists to store data
# date = []
# profit_loss = []

# with open(budget_data_csv, encoding='utf-8') as csvfile:
with open(budget_data_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

#         # Add date
#         date.append(row[0])

#         # Add profit_loss
#         profit_loss.append(row[1])

#         # # Determine poverty rate to 2 decimal places, convert to string
#         # percent = round(int(row[8]) / int(row[1])*100, 2)
#         # poverty_rate.append(str(percent)+"%")

#         # # Split the place into county and state
#         # split_place = row[0].split(", ")
#         # # print(split_place)
#         # county.append(split_place[0])
#         # state.append(split_place[1])

# # Zip lists together
# cleaned_data = list(zip(date, profit_loss))

# # Set variable for output file
# output_file = os.path.join("PyBank_analysis.csv")

# #  Open the output file
# with open(output_file, "w", newline='') as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Date", "Profit/Losses"])

#     # Write in zipped rows
#     writer.writerows(cleaned_data) 