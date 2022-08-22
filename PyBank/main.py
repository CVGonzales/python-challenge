import os
import csv

os.chdir(os.path.dirname(__file__))

budget_csv = os.path.join("Resources", "budget_data.csv")

months_total = []
profit_total = []
monthly_change_profit = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        months_total.append(row[0])
        months_sum = len(months_total)

        profit_total.append(int(row[1]))
        profit_sum = sum(profit_total)


print("Financial Analysis")
print("------------------------------------------------------")
print(f'Total Months: {months_sum}')
print(f'Total: ${profit_sum}')
print(f'Average Change:')
print(f'Greatest Increase in Profits:')
print(f'Greatest Decrease in Profits:')