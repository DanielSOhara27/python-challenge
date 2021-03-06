# Adding Dependendancies
import os
import csv
import pandas as pd # Instructions do not explicitly forbid the use of pandas, therefore I assume it is permitted

# Setting up filepath using os library
filePath = os.path.join("Resources", "election_data.csv")
winner = ''
winnerNum = 0
outputList = list()

# Reading ocntents of the csv file and converting it into a dataFrame
df = pd.read_csv(filePath, encoding="ISO-8859-1")

# Getting votes distributed per Candidate
candidateVotes = (df['Candidate'].value_counts()).to_dict()

# Getting total votes
totalVotes = df['Candidate'].count()
# print(candidateVotes)

outputList.append(f"\nElection Results\n{'-'*30}\nTotal Votes: {df['Candidate'].count()}\n{'-'*30}")

for i in candidateVotes:

    # Keeping track of winner
    if( winnerNum < candidateVotes[i]):
        winnerNum = candidateVotes[i]
        winner = i
    outputList.append(f"{i}: {round((candidateVotes[i]/totalVotes)*100)}% ({candidateVotes[i]})")

outputList.append(f"{'-'*30}\nWinner: {winner}\n{'-'*30}")

for x in outputList:
    print(x)

with open("Output_Election_Data.txt", "w+") as outputFile:
    outputFile.writelines("%s\n" %line for line in outputList)
