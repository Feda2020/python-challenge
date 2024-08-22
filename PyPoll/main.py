#Importing the os module
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module

#Variables for the candidates, and winning votes
candidates = {}
winner = ""
winning_votes = 0

with open(csvpath , 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #To skip the header row
    next(csvreader)

    #Store the data in a list
    data = list(csvreader)
    #Count the total number of votes 
    total_votes = len(data)
    
    #Iterate over rows to check candidates
    for row in data:
    #Candidate is in the 3rd column
        candidate = row[2]

        #if candidcate is in the file, count their votes
        if candidate in candidates:
            candidates[candidate] += 1

        #if candidate is not in the file, add them with count of 1
        else:
            candidates[candidate] = 1
    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
# Determining the percentage of votes each candidate got and finding the winner
    for candidate, votes in candidates.items():

    #To calculate the votes percentage
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% and {votes}\n")
        #Finding the winner
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate


    #printing the data title then printing a line
    
    
    print("--------------------------------")
    print(f"Winner: {winner}")