#Importing the os module
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

#Getting variables for profit/losses, change, greatest inc. and greatest dec.

total = 0
previous_profit_losses = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}
months = []

with open(csvpath , 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #To skip the header row
    next(csvreader)

    #Store the data in a list
    data = list(csvreader)
    #Count the total number of months 
    total_months = len(data)
    
    #Calculate the net total amount of profit/losses
    for row in data:
        date = row[0]
        profit_losses = int(row[1])
        total += profit_losses
    
    # Skip the first month since there's no previous month to compare
        if previous_profit_losses is not None:  
            change = profit_losses - previous_profit_losses
            changes.append(change)
            months.append(date)

        # Update the previous profit/losses
        previous_profit_losses = profit_losses

# Calculate the average change in "Profit/Losses"
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding months for the greatest increase and decrease
greatest_increase_month = months[changes.index(greatest_increase)]
greatest_decrease_month = months[changes.index(greatest_decrease)]

    #printing the data title then printing a line
print("Finanacial Analysis")

print("--------------------------------")
    #print the total number of months
print(f"Total number of months: {total_months}")

print(f"Net Total Amount of 'Profit/Losses': ${total}")
print(f"Average Change in 'Profit/Losses': ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
