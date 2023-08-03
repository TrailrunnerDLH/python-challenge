#Import CSV
import csv
#create variable to store file name
data_file = 'resources/budget_data.csv'

# Create Variables to do calculations 
sum = 0
sum_of_changes = 0
previous_profit_loss = 0
max_change = 0 
min_change = 0
max_date = ""
min_date = ""

i=0

#loop through list
with open (data_file, "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
       #Skip header row
        if i > 0:
            #Append the current profit/loss to the sum
            current_profit_loss = int(row[1])
            sum = sum + current_profit_loss 

            # Skip second row for the first line of data ( no change in previous period)
            if i > 1:
                #Calculate change for current period and append to sum of changes 
                change = current_profit_loss - previous_profit_loss
                sum_of_changes = sum_of_changes + change

                #Loop through list and keep max change and date
                if change > max_change:
                    max_change = change
                    max_date = row[0]
                
                #Loop through list and keep min change and date
                if change < min_change:
                    min_change = change
                    min_date = row[0]

            # store this row's profit loss for next iteration
            previous_profit_loss = current_profit_loss
        #increase index by one
        i = i + 1
#reduce index by one ( header). This equals the number of periods.
count = i - 1

#Divide sum of changes by the number of changes to get average of all changes
change_average = sum_of_changes / (count-1)

#print calculated values
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(count))
print ("Total: $" + str(sum))
print (f'Average Change: ${change_average:.2f}')
print("Greatest Increase in Profits: " + max_date  + " ($" + str(max_change)+")")
print("Greatest Decrease in Profits: " + min_date  + " ($" + str(min_change)+")")

#Print same values into text file
with open( "analysis/analysis.txt", "w") as f:
    print ("Financial Analysis", file=f)
    print ("----------------------------", file=f)
    print ("Total Months: " + str(count), file=f)
    print ("Total: $" + str(sum), file=f)
    print (f'Average Change: ${change_average:.2f}', file=f)
    print("Greatest Increase in Profits: " + max_date  + " ($" + str(max_change)+")", file=f)
    print("Greatest Decrease in Profits: " + min_date  + " ($" + str(min_change)+")", file=f)

