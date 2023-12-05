# First we'll import the os module
import os

# Module for reading CSV files
import csv

# set path for file
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    # reading data in dictionary form
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # making a list of dictionaries
    election_data = list(csvreader)

    # storing ballot ID values in list. storing candidate values in list
    Ballot_ID = [row["Ballot ID"] for row in election_data]
    Candidate = [row["Candidate"] for row in election_data]

    # initializing total ballot id variable to 0
    total_Ballot_ID = 0

    # loop through IDs and get total count 
    for ID in Ballot_ID :
        total_Ballot_ID = total_Ballot_ID+1

    # create empty list to store the candidates who have votes
    candidates_with_votes = []

    # loop through the people in the candidates list --> if the candidate is not already found in the candidates with votes list, add them.
    for people in Candidate:
        if people not in candidates_with_votes:
            candidates_with_votes.append(people)

    # create empty list to store total number of votes for each candidate
    candidate_votes_totals = []

    # initialize candidate vote counts to 0
    count_Stockham = 0
    count_DeGette = 0
    count_Doane = 0

    # loop through each person in candidates list
    for person in Candidate:
        # if the person has this name, add to their count
        if (person == "Charles Casper Stockham"):
            count_Stockham = count_Stockham + 1
        # if the person has this name, add to their count
        if (person == "Diana DeGette"):
            count_DeGette = count_DeGette + 1
        # if the person has this name, add to their count
        if (person == "Raymon Anthony Doane"):
            count_Doane = count_Doane + 1

    # add the count totals to the candidate votes totals list
    candidate_votes_totals.append(count_Stockham)
    candidate_votes_totals.append(count_DeGette)
    candidate_votes_totals.append(count_Doane)

    # create empty list to store the percents of the vote totals for each candidate
    percent_candidate_votes_totals = []

    # calculate the percents of vote totals for each candidate
    percent_Stockham = (count_Stockham/total_Ballot_ID)*100
    percent_DeGette = (count_DeGette/total_Ballot_ID)*100
    percent_Doane = (count_Doane/total_Ballot_ID)*100

    # add the percents for each candidate to the percent_candidate_votes_totals list
    percent_candidate_votes_totals.append(percent_Stockham)
    percent_candidate_votes_totals.append(percent_DeGette)
    percent_candidate_votes_totals.append(percent_Doane)

    # build dictionary with candidates with votes, percents of vote totals, and candidate vote totals
    candidate_summary_dictionary = dict(zip(candidates_with_votes, zip(percent_candidate_votes_totals, candidate_votes_totals)))

    # find largest value in the candidate summary dictionary, and get the key. this will be candidate that has largest votes
    winner_election_key = max(candidate_summary_dictionary, key=candidate_summary_dictionary.get)

    # Specify the file to write to
    output_path = os.path.join("..", "PyPoll", "analysis", "analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as txtfile:
        # write analysis in text file
        txtfile.write('Election Results')
        txtfile.write('\n')
        txtfile.write('------------------------------------------------------------------------------')
        txtfile.write('\n')
        txtfile.write('Total Votes: ')
        txtfile.write(str(total_Ballot_ID))
        txtfile.write('\n')
        txtfile.write('------------------------------------------------------------------------------')
        txtfile.write('\n')

        # loop through each key in dictionary to write each key/value on a separate line
        for key in candidate_summary_dictionary.keys():
            txtfile.writelines (f"'{key}': '{candidate_summary_dictionary[key]}',\n")

        txtfile.write('------------------------------------------------------------------------------')
        txtfile.write('\n')
        txtfile.write('Winner: ')
        txtfile.write(winner_election_key)
        txtfile.write('\n')
        txtfile.write('------------------------------------------------------------------------------')

    # print analysis to terminal
    print("Election Results")
    print("------------------------------------------------------------------------------")
    print("Total Votes: ", total_Ballot_ID)
    print("------------------------------------------------------------------------------")

    # loop through each key in summary dictionary to print each key/value to new line
    for key in candidate_summary_dictionary:
        print (f"{key}: {candidate_summary_dictionary[key]}")

    print("------------------------------------------------------------------------------")
    print("Winner: ", winner_election_key)
    print("------------------------------------------------------------------------------")