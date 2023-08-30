#Import CSV
import csv
#create variable to store file name
data_file = 'resources/election_data.csv'

# Create Variables to do calculations 

candidates = {}
i=0

#loop through list
with open (data_file, "r") as csvfile:
    datareader = csv.reader(csvfile)

    for row in datareader:
        if i > 0:
            candidate = row[2]
            if candidate in candidates:
                candidates[candidate] = candidates[candidate] + 1
            else:
                candidates[candidate] = 1
        i = i + 1

count = i - 1 
            
# print total votes and by candidate
print ("Election Results")
print ("----------------")
print ("Total Votes: " + str(count)) 
print ("----------------")

#loop through candidate for votes and percent
for key, value in candidates.items():
    percent_votes = value/count*100
    print (key + ": " + f'{percent_votes:.2f}' + "% (" + str(value) + ")")

# create variables to determine winner
max_votes = 0
winner = ''

#loop through to calculate winner
for key, value in candidates.items():

    if value > max_votes:
        max_votes = value
        winner = key


print ("----------------")
print ("Winner: " +  winner) 

#Print same values into text file
with open( "analysis/analysis.txt", "w") as f:
    print ("Election Results",file=f)
    print ("----------------", file=f)
    print ("Total Votes: " + str(count),file=f) 
    print ("----------------",file=f)
    for key, value in candidates.items():
        percent_votes = value/count*100
        print (key + ": " + f'{percent_votes:.2f}' + "% (" + str(value) + ")",file=f)
    print ("----------------",file=f)
    print ("Winner: " +  winner,file=f)    