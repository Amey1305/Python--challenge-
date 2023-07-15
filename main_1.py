import os
import csv

#Set path for csv file
budget_date_csv = os.path.join("budget_data.csv")
final_analysis = os.path.join("Budget_analysis.txt")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Read the dataset file
with open(budget_date_csv, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  

    # Iterate through each row in the dataset
    for row in csv_reader:
        # Get the date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount
        net_total += profit_loss

        # Calculate the change in profit/loss
        change = profit_loss - previous_profit
        total_change += change

        # Update the greatest increase and decrease values
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date

        # Update the previous profit/loss value
        previous_profit = profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)

#calculate final output to print
result = (f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print the financial analysis result
print(result)

#write result in txt file 
with open(final_analysis,"w") as txt_file:
    txt_file.write(result)


     

    
    





