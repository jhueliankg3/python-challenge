import os
import csv

#Create file path for polling data
election_csv = os.path.join("election_data.csv")

#Use dictionary for candidate name and vote count
poll = {}

# Set variable "total votes" to zero
total_votes = 0

#Retrieve csv 
with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)


#Make dictionary from data using the third column as the key (use names once)
#Count votes for each candidate as entries
#keep a total vote count by counting +1 for each loop (#rows w/o header)

    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

#Use empty lists for candidates and vote count
candidates = []
vote_count = []

#Use dictionary keys and values by placing them in into lists
# vote_count and candidates

for key, value in poll.items():
    candidates.append(key)
    vote_count.append(value)

#Vote Percent List
vote_percent = []
for n in vote_count:
    vote_percent.append(round(n/total_votes*100, 1))

#clean the data using zips
clean_data = list(zip(candidates, vote_count, vote_percent))

#Make winner list (includes ties)
winner_list = []

for name in clean_data:
    if max(vote_count) == name[1]:
        winner_list.append(name[0])

# Make list a string
winner = winner_list[0]

#Runs only if there is a tie and places additional winners into string seperated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + "," + winner_list[w]

#Print to file
output_file = os.path.join("PyPoll" + ".txt")

with open(output_file, "w") as txtfile:
    txtfile.writelines("Election Results \n-----------------\n Total Votes: " + str(total_votes) + "\n-----------------\n")
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) + '% (' + str(entry[1]) + ')\n')
        
with open (output_file, "r") as readfile:
    print(readfile.read())
