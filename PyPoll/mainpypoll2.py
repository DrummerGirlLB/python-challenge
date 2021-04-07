#The total number of votes cast 
#A complete list of candidates who received votes 
#The percentage of votes each candidate won 
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv


csv_file = os.path.join('PyPollCSV.csv')
csv_output = os.path.join("PyPollAnalysis.txt")

list_candidates = []
count_votes = []
percent_votes = []
total_votes = 0
count_winner = 0

def fixtopercent(num):
    num = "{:.3%}".format(num)
    return num

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
#print (winner)
#ok, now just have to write the output file
#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
with open(csv_output, 'w') as textfile:
    textfile.write(f" Election Results! \n"
            f"*********************** \n"
            f"We received {total_votes} total votes\n"
            f"*********************** \n"
            )
        
    for i in range(len(list_candidates)):
        textfile.write(f"{list_candidates[i]}: {fixtopercent(percent_votes[i])} ({count_votes[i]}) \n")
    
    textfile.write(f"***************** \n"
        f"The winner is: {winner}\n"
        f"***************** \n"
        )

with open (csv_output, 'r') as analysis:
    content = analysis.read()
print (content)