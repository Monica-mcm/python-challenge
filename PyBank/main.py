import os
import csv
from datetime import datetime

#Read csv file
budget_csv= os.path.join('..', 'PyBank', 'budget_data.csv')

with open (budget_csv, newline = '') as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')
    print (csvreader)
#Read the header firsr
    csv_header = next (csvfile)
    print (f"Headers: {csv_header}")
#Inicial text  
    print ("Finantial Analysis")
    print ("-----------------------------")

#Two columns: Date and Profit / Looses
    for row in csvreader
    date_row = (row[0])
    profit_looses = (row [1])
    
#Calculate total number of months included in the dataset

date = datetime.strptime(row[0],'%m/%d/%Y')
print(date)

#Calulate the net total amount of "Profit/Looses" over the entire period
#Calculate the average of changes in "Profir/Looses" over the entire period
#Calculate the greatest increase in profits (date and amount) over the entire period
#Calculate the greates decrease in looses (date and amount) over the entire period
#Your script should export a text file with the results