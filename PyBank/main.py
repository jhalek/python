import os
import csv

csvpath = os.path.join('budget_data.csv')
csvpath2 = os.path.join('output.csv')

dates = []
values = []
changevalues = []
x = "!"
y = 0
maxchangedate = 'test'

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        #create list of dates
        dates.append(row[0])
        
        #create list of profit values
        values.append(row[1])
        
        #convert list of string values to integers
        valuesint = [int(i) for i in values]
        
        if x != "!":

            y = int(row[1]) - x
        
            changevalues.append(y)
        
        x = int(row[1])
        

    avgchange = sum(changevalues) / int(len(changevalues))
    total_months = len(dates)
    sum_profitloss = sum(valuesint)
    maxchange = max(changevalues)
    minchange = min(changevalues)
    changevalues.insert(0, 0)
    

roster = zip(dates, values, changevalues)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Dates", "Values", "Change Values"])

    writer.writerows(roster)

with open(csvpath2, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        
        if int(row[2]) == maxchange:
            maxchangedate = row[0]
            
        if int(row[2]) == minchange:
            minchangedate = row[0]
    
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(sum_profitloss))
print("Avg Change: $" + str(avgchange))
print("Greatest Increase in Profits: " + str(maxchangedate) + " " + str(maxchange))
print("Greatest Decrease in Profits: " + str(minchangedate) + " " + str(minchange))

f = open('Financial Analysis.txt','w')
f.write("Financial Analysis")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write("Total Months: " + str(total_months))
f.write("\n")
f.write("Total: $" + str(sum_profitloss))
f.write("\n")
f.write("Avg Change: $" + str(avgchange))
f.write("\n")
f.write("Greatest Increase in Profits: " + str(maxchangedate) + " " + str(maxchange))
f.write("\n")
f.write("Greatest Decrease in Profits: " + str(minchangedate) + " " + str(minchange))
f.close()
    