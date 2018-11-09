import csv


# Files load and output 
file_to_load = "raw_data/budget_data.csv"
file_to_output = "analysis.txt"

# track various profit parameters
total_months = 0
total_amount = 0
previos = 0
month_change = []
profit_change_list = []
max_increase = 0 
max_decrease = 0

# read the csv convert into a list of dictionaries 
with open(file_to_load) as profit_data:
    reader = csv.DictReader(profit_data)

    for row in reader:

        # track total
        total_months = total_months + 1 
        total_amount = total_amount + int(row["Profit/Losses"])


        if total_months > 1:
            change = int(row["Profit/Losses"])-previos
            month_change.append(change)

            if change > max_increase:
                max_increase = change
                max_increase_month = row["Date"]

            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row["Date"]

        previos = int(row["Profit/Losses"])

# Calculate the average profit change

average = round(sum(month_change)/(len(month_change)+ 0.0),2)

output = ('Financial Analysis'+ '\n'+
          '.........................'+ '\n'  +
          'Total Months: ' + str(total_months) + '\n' +
          'Total: ' + ' $'+ str(total_amount) + '\n' +
          'Average Change:' + ' $' + str(average) + '\n' +
          'The Greatest Increase in Profits: ' + max_increase_month + ' $' + str(max_increase) + '\n' +
          'The Greatest Decrease in Profits: ' + max_decrease_month + ' $' + str(max_decrease) + '\n')

      

print(output)

with open(file_to_output, 'w') as outputfile:
    outputfile.write(output)

