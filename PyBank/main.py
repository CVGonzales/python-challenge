import os
import csv

os.chdir(os.path.dirname(__file__))

budget_csv = os.path.join("Resources", "budget_data.csv")

month = []
profit_total = []
monthly_change_profit = []
average_change = []


with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        month.append(row[0])
        months_total = len(month)

        profit_total.append(int(row[1]))
        profit_sum = sum(profit_total)

    for row in range(0,len(profit_total)-1):
        monthly_change_profit.append(int(profit_total[row+1]-int(profit_total[row])))
        average_change = round(sum(monthly_change_profit)/ len(monthly_change_profit), 2)

    great_inc = max(monthly_change_profit)
    great_dec = min(monthly_change_profit)
    month_great_inc = month[monthly_change_profit.index(great_inc)+1]
    month_great_dec = month[monthly_change_profit.index(great_dec)+1]


print("Financial Analysis")
print("------------------------------------------------------")
print(f'Total Months: {months_total}')
print(f'Total: ${profit_sum}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_great_inc} (${great_inc})')
print(f'Greatest Decrease in Profits: {month_great_dec} (${great_dec})')


output_path = os.path.join("analysis", "bankresults.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis" + '\n')
    txtfile.write("------------------------------------------------------" + '\n')
    txtfile.write(f'Total Months: {months_total}' + '\n')
    txtfile.write(f'Total: ${profit_sum}' + '\n')
    txtfile.write(f'Average Change: ${average_change}' + '\n')
    txtfile.write(f'Greatest Increase in Profits: {month_great_inc} (${great_inc})' + '\n')
    txtfile.write(f'Greatest Decrease in Profits: {month_great_dec} (${great_dec})' + '\n')