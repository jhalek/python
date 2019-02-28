
#os.getcwd()

import os
import csv

os.chdir('C:\\Users\\jhalek\\Desktop\\cwrubootcamp\\python-challenge\\PyPoll')

csvpath = os.path.join('..','PyPoll','03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
csvpath2 = os.path.join('..','PyPoll','output.csv')

totalvotes = []
khanlist = []
correylist = []
lilist = []
otooleylist = []
allcandidates = []
allcandidates2 = []
khan = 'null'
correy = 'null'
li = 'null'
otooley = 'null'
winning_candidate = 'null'

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        totalvotes.append(row[0])
        
        if (row[2]) == 'Khan':
            khanlist.append(row[1])
            khan = 'Khan'
        elif (row[2]) == 'Correy':
            correylist.append(row[1])
            correy = 'Correy'
        elif (row[2]) == 'Li':
            lilist.append(row[1])
            li = "Li"
        elif (row[2]) == "O'Tooley":
            otooleylist.append(row[1])
            otooley = "O'Tooley"
           
khan_votes = len(khanlist) 
allcandidates.append(khan_votes)
correy_votes = len(correylist)
allcandidates.append(correy_votes)
li_votes = len(lilist)
allcandidates.append(li_votes)
otooley_votes = len(otooleylist)         
allcandidates.append(otooley_votes)

          
khan_votes_per = len(khanlist) / len(totalvotes)
correy_votes_per = len(correylist) / len(totalvotes)
li_votes_per = len(lilist) / len(totalvotes)
otooley_votes_per = len(otooleylist) / len(totalvotes)     

allcandidates2 = (khan, correy, li, otooley)           
winner = max(allcandidates)

roster = zip(allcandidates2, allcandidates)

output_file = os.path.join("output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Cadidates","Total Votes"])
    
    writer.writerows(roster)

with open(csvpath2, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        
        if int(row[1]) == winner:
            winning_candidate = row[0]
            
            
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(len(totalvotes)))
print("----------------------------")
print("Khan: " + str(float(round(khan_votes_per * 100))) + "%" + " " + "(" + str(khan_votes)+")")
print("Correy: " + str(float(round(correy_votes_per * 100))) + "%" + " " + "(" + str(correy_votes)+")")
print("Li: " + str(float(round(li_votes_per * 100))) + "%" + " " + "(" + str(li_votes)+")")
print("O'Tooley: " + str(float(round(otooley_votes_per * 100))) + "%" + " " + "(" + str(otooley_votes)+")")
print("----------------------------")
print("Winner: " + winning_candidate)
print("----------------------------")

f = open('election_results.txt','w')
f.write("Election Results")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write("Total Votes: " + str(len(totalvotes)))
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write("Khan: " + str(float(round(khan_votes_per * 100))) + "%" + " " + "(" + str(khan_votes)+")")
f.write("\n")
f.write("Correy: " + str(float(round(correy_votes_per * 100))) + "%" + " " + "(" + str(correy_votes)+")")
f.write("\n")
f.write("Li: " + str(float(round(li_votes_per * 100))) + "%" + " " + "(" + str(li_votes)+")")
f.write("\n")
f.write("O'Tooley: " + str(float(round(otooley_votes_per * 100))) + "%" + " " + "(" + str(otooley_votes)+")")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write("Winner: " + winning_candidate)
f.write("\n")
f.write("----------------------------")
f.close()

