#import libraries for os and csv
import os
import csv

#create path to data file
csv_file = os.path.join("PyBankCSV.csv")

#create lists for both headers and for monthly P/L changes
profit_loss = []
pl_changes_monthly = []
months = []

#create counters
countmonths = 0
total_profit = 0
total_changes_monthly = 0
start_profit = 0

#newline="" always include - just because from what I read
with open(csv_file, newline="") as csvfile: 

#read the separated columns (usually good to call the delimiter but will default to ","    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)

#append row data to lists and apply some math
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(row[1])
        total_profit = total_profit + int(row[1])
        countmonths = countmonths + 1
        
        end_profit = int(row[1])
        monthly_changes = end_profit - start_profit
        
        pl_changes_monthly.append(monthly_changes)
        
        total_changes_monthly = total_changes_monthly + monthly_changes
        start_profit = end_profit
        
        avg_change_profit = (total_changes_monthly/countmonths)

        max_increase_profit = max(pl_changes_monthly)
        max_decrease_profit = min(pl_changes_monthly)
        
        up_date = months[pl_changes_monthly.index(max_increase_profit)]
        down_date = months[pl_changes_monthly.index(max_decrease_profit)]
        
    print ("Here is your financial analysis")
    print ("Get ready, it's gonna be a fun one! ")
    print ("--------------------------------------")
    print ("Total number of months: " + str(countmonths))
    print ("Your total profits were: " + "$" + str(total_profit))
    print ("The average change monthly was: " + "$" + str(int(avg_change_profit)))
    print ("Your greatest increase was: " + str(up_date) + "   $" + str(int(max_increase_profit)))
    print ("Your greatest decrease was: " + str(down_date) + "   $" + str(int(max_decrease_profit)))
    
with open('analysis.txt', 'w') as text:
    text.write ("Here is your financial analysis" + "\n")
    text.write ("Get ready, it's gonna be a fun one!" + "\n")
    text.write ("--------------------------------------\n")
    text.write ("Total number of months: " + str(countmonths) + "\n")
    text.write ("Your total profits were: " + "$" + str(total_profit) + "\n")
    text.write ("The average change monthly was: " + "$" + str(int(avg_change_profit)) + "\n")
    text.write ("Your greatest increase was: " + str(up_date) + "   $" + str(int(max_increase_profit)) + "\n")
    text.write ("Your greatest decrease was: " + str(down_date) + "   $" + str(int(max_decrease_profit)) + "\n")
    text.write ("And there you have it. Have a great day!")