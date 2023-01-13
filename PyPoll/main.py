#Import Required Libraries

import os
import csv

#Create required candidate lists
Stockham=[]
DeGette=[]
Doane=[]

#Point to election_data CSV file
poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #remove header and store it as a variable
    header=next(csvreader)
    
    #Append instances of votes matching each candidate to their respective lists
    for row in csvreader:

        if row[2]=="Charles Casper Stockham":
            Stockham.append(row[2])

        if row[2]=="Diana DeGette":
            DeGette.append(row[2])

        if row[2]=="Raymon Anthony Doane":
            Doane.append(row[2])

#perform calculations for total votes and percentage of votes for each candidate
total = len(Stockham)+len(DeGette)+len(Doane)
percent_Stockham= round(100*len(Stockham)/total, 3)
percent_DeGette= round(100*len(DeGette)/total, 3)
percent_Doane= round(100*len(Doane)/total, 3)

#use conditionals to determine the winner based on largest percentage
if percent_Stockham > percent_DeGette or percent_Stockham> percent_DeGette:
        winner = "Charles Casper Stockham"
elif percent_DeGette>percent_Stockham or percent_DeGette>percent_Doane:
        winner = "Diana DeGette"
else:
        winner = "Raymon Anthony Doane"

#create output file 
poll_final = os.path.join("analysis", "poll_final.csv")
#  Open the output file and input required data
with open(poll_final, "w") as f:
    print("Election Results")
    f.write("Election Results \n")

    print("----------------------------")
    f.write("----------------------------\n")

    print(f"Total Votes: {total}")    
    f.write("Total Votes: " + str(total) + '\n')

    print("----------------------------")
    f.write("----------------------------\n")

    print(f"Charles Casper Stockham: {percent_Stockham}% ({len(Stockham)})")
    f.write("Charles Casper Stockham: " + str(percent_Stockham) + "% (" + str(len(Stockham)) + ") \n")

    print(f"Diana DeGette: {percent_DeGette}% ({len(DeGette)})")
    f.write("Diana DeGette: " + str(percent_DeGette) + "% (" + str(len(DeGette)) + ") \n")

    print(f"Raymon Anthony Doane: {percent_Doane}% ({len(Doane)})")
    f.write("Raymon Anthony Doane: " + str(percent_Doane) + "% (" + str(len(Doane)) + ") \n")

    print("----------------------------")
    f.write("----------------------------\n")

    print(f"Winner: {winner}")    
    f.write("Winner: " + str(winner) + '\n')

    print("----------------------------")
    f.write("----------------------------\n")