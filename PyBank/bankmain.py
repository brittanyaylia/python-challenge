#import modules
import csv
import os

#path to csv
budget_csv = os.path.join("./Resources/budget_data.csv")

#starting parameters
total_months = 0 
total_revenue = 0 
greatest_increase = 0 
greatest_increase_month = 0 
greatest_decrease = 0 
greatest_decrease_month = 0 
month_changes = []
month_count = []

#open and read csv
with open(budget_csv, newline = '') as finance_data:

    #specify delimiter & variable 
    csvreader = csv.reader(finance_data, delimiter=',')
    
    #read and skip header
    header = next(csvreader)
    row = next(csvreader)

    #calculate total of months 
    total_months += 1

    #set variables for rows
    past_profit_row = int(row[1])
    total_revenue += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #read ea. row after header
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])

        #calculate the mo/mo profit change
        profit_change = int(row[1]) - past_profit_row 
        month_changes.append(profit_change)
        past_profit_row = int(row[1])
        month_count.append(row[0])

        #calculate the greatest profit increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #calculate the greatest profit decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #calculate the average change and date
    av_change = sum(month_changes)/len(month_changes)

    maximum = max(month_changes)
    minimum = min(month_changes)

    #print values 
    print("Financial Analysis")
    print("-------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(int(av_change)))
    print(greatest_increase_month, max(month_changes))
    print(greatest_decrease_month, min(month_changes))

    #txt file 
    PyBank = open("./Analysis/budget_analysis.txt", "w+")
    PyBank.write("Financial Analysis")
    PyBank.write('\n ---------------------------------------')
    PyBank.write('\n' + "Total Months: " + str(total_months))
    PyBank.write('\n' + "Total Amount: " + "$" + str(total_revenue))
    PyBank.write('\n' + "Average Change: " + "$" + str(av_change))
    PyBank.write('\n' + "Greatest Increase in Profits: " + str(greatest_increase_month) + " $" + str(maximum))
    PyBank.write('\n' + "Greatest Decrease in Profits: " + str(greatest_decrease_month) + " $" + str(minimum))



    





