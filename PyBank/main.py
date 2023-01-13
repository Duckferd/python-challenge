#Import Required Liiraries
import os
import csv

# Created required lists to store data
date = []
profit = []
change=[]

#Point to budget_data CSV file
budget_csv = os.path.join("Resources", "budget_data.csv")
#Open the file and extract some initial columns
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #remove and store the header separately under "header" string
    header=next(csvreader)

#Append date and profit rows to their own lists
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add profit
        profit.append(int(row[1]))

#Create profit change list by using enumeration to subtract current row from previous row
for x, row in enumerate(profit):
    #this if statement is required because the first row of the change list would be empty/invalid
    #could also just change.pop(0) to work
    if x>0:
        change.append(profit[x]-profit[x-1])


#create output file 
budget_final = os.path.join("analysis", "budget_final.csv")
#  Open the output file and input required data
with open(budget_final, "w") as f:
    print("Financial Analysis")
    f.write("Financial Analysis \n")

    print("----------------------------")
    f.write("----------------------------\n")

    print(f"Total Months: {len(date)}")    
    f.write("Total Months: " + str(len(date)) + '\n')

    print(f"Total: {sum(profit)}")
    f.write("Total: " + str(sum(profit)) + '\n')

    print(f"Average Change: {round(sum(change)/len(change), 2)}")
    f.write("Average Change: " + str(round(sum(change)/len(change), 2)) + '\n')

    for i, row in enumerate(change):
        #the date[] rows should skip first row, to align with the invalid first row in "change" list.
        if change[i]<=min(change):
            print(f"Greatest Decrease in Profits: {date[i+1]} (${min(change)})")
            f.write("Greatest Decrease in Profits: " + str(date[i+1]) + " ($" + str(min(change)) + ") \n")
        if change[i]>=max(change):
            print(f"Greatest Decrease in Profits: {date[i+1]} (${max(change)})")
            f.write("Greatest Decrease in Profits: " + str(date[i+1]) + " ($" + str(max(change)) + ") \n")