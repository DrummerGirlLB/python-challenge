#The total number of votes cast 
                #num_total_votes
#A complete list of candidates who received votes 
                #list_candidates
#The percentage of votes each candidate won 
                #percentage_candidate
#The total number of votes each candidate won
                #num_votes_candidate
#The winner of the election based on popular vote
                #winner_candidate

import os
import csv

csv_file = os.path.join('PyPollCSV.csv')

#try a function
def polldata(pypollcsv):
    num_total_votes = 0
    votes_candidate = []
    candidates = []
    list_candidates = []
    percent_votes_candidates = []
    winner_candidate = []

    for row in pypollcsv:
        num_total_votes += 1
    
        if row[2] not in list_candidates:
            list_candidates.append(row[2])
            votes_candidate.append(row[2])
    
    for candidate in list_candidates:
        candidates.append(votes_candidate.count(candidate))
        percent_votes_candidate.append(round(votes_candidate.count(candidate)/num_total_votes*100,3))
 
        winner_candidate = list_candidates[candidate.index(max(candidate))]
 
    
with open(csv_file, newline="") as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)

print (winner_candidate)
