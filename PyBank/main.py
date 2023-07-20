# Importing pandas lib
import pandas as pd
#create variable to store file name
data_file = 'resources/budget_data.csv'

#read in csv file and store in variable
csvfile = pd.read_csv(data_file)
# Variables 
sum = 0

#
for i, row in csvfile.iterrows():
    print (i)
    print (row [1]) 
    sum = sum + (row[1]) 


#print header and number of rows of data
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(len(csvfile)))
print ("Total: $" + str(sum))



