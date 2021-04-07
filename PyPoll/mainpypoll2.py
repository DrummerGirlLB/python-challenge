#The total number of votes cast 
#A complete list of candidates who received votes 
#The percentage of votes each candidate won 
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

csv_file = os.path.join('PyPollCSV.csv')
outputfile = os.path.join("PyPollAnalysis.txt")

list_candidates = []
count_votes = []
percent_votes = []
total_votes = 0
count_winner = 0

with open(csv_file, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    header = next(reader)
    
    for row in reader:
        total_votes += 1

#append unique candidates/count         
        if row[2] not in list_candidates:
            list_candidates.append(row[2])
            count_votes.append(1)

#append candidate/count            
        else:
            candidate_index = list_candidates.index(row[2])
            count_votes[candidate_index] += 1

#calculate percentages for candidates
for i in range(len(count_votes)):
    percent_votes.append(count_votes[i] / total_votes)
    
#find candidate with most votes
for i in range(len(count_votes)):
    if count_votes[i] > count_winner:
        count_winner = count_votes[i]
        winner = list_candidates[i]
print (winner)