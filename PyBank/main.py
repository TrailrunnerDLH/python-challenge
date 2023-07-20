# Importing pandas lib
import pandas as pd
#create variable to store file name
data_file = 'resources/budget_data.csv'

#read in csv file and store in variable
csvfile = pd.read_csv(data_file)
# Variables 
sum = 0
sum_of_changes = 0
previous_profit_loss = 0

#loop through list
for i, row in csvfile.iterrows():
    print (i)
    # print (row [1]) 
    current_profit_loss = row[1]
    sum = sum + current_profit_loss 

    if i > 0:
        change = current_profit_loss - previous_profit_loss
        sum_of_changes = sum_of_changes + change
        # print(change)


    previous_profit_loss = current_profit_loss

change_average = sum_of_changes / (len(csvfile)-1)
#print header and number of rows of data
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(len(csvfile)))
print ("Total: $" + str(sum))
print (f'Average Change: ${change_average:.2f}')



