print('AVERAGE RAINFALL CALCULATOR')
print('----------------\n')

total_years = int(input('Enter the amount of years: '))

for years in range(total_years):
    total = 0.0
    print('----------------')
    print('Year', years + 1)
    print('----------------')
    for month_number, month in enumerate(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), start=1):
        inches = float(input(f'How many inches did it rain for year {years + 1}, month {month_number} ({month})? '))
        total += inches

total_inches = total
total_month = total_years * 12
average_inches = round(total / total_month,2)

print('The total number of months is: ', total_month)
print('The total inches of rainfall is: ', total_inches)
print('The average rainfall per month for the entire period is: ', average_inches)
