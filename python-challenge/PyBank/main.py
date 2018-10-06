import os
import csv

#create file path
budget_csv = os.path.join("budget_data.csv")

#list data storage
months = []
revenue = []

#Read csv and append both columns indicate revenue as a list of integers
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

# find total months
total_months = len(months)

# make variables for greatest increase and decrease in revenue 
total_revenue = 0
greatest_inc = revenue[0]
greatest_dec = revenue[0]

# loop through rev. indices and compare to find greatest increase and decrease
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

# calculate average change
average_change = round(total_revenue/total_months, 2)

output_path = os.path.join("PyBank" + ".txt")

with open(output_path, "w") as writefile:
    writefile.writelines('Financial Analysis' + '\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: '+ str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')' + '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' +str(greatest_dec) + ')')

with open(output_path, "r") as readfile:
    print(readfile.read())