#Importing the os module
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath , 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #To skip the header row
    next(csvreader)

    #Count the total number of votes 
    
    total_votes = sum(1 for row in csvreader)
    
    #printing the data title then printing a line
    print("Election Results")

    print("--------------------------------")
    #print the total number of months
    print(f"Total number of months: {total_votes}")

    print("--------------------------------")
