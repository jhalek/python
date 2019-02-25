import os
import csv

csvpath = os.path.join('Desktop','cwrubootcamp','python-challenge','PyBank','budget_data.csv')

dates = []
values = []
changevalues = []
x = 0
y = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        #create list of dates
        dates.append(row[0])
        
        #create list of profit values
        values.append(row[1])
        
        #convert list of string values to integers
        valuesint = [int(i) for i in values]
        
        y = int(row[1]) - x
        
        changevalues.append(y)
        
        x = int(row[1])
        
            
    avgchange = sum(changevalues) / int(len(changevalues))
    total_months = len(dates)
    sum_profitloss = sum(valuesint)
    print(changevalues)
    print(avgchange)
    print(total_months)
    print(sum_profitloss) 
    
    