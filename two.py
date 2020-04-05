# Allow user to input number of people to divide a check evenly

total_bill = float(input('What is the total bill amount? '))
service_level = input('Level of service? Good, fair, or bad? ')
split_check = float(input('Split how many ways? '))

tip_text = 'Tip amount: '
tip = 0.0

total = 'Total amount: '

if service_level == 'good':
    tip = float(total_bill * 0.2)
elif service_level == 'fair':
    tip = float(total_bill * 0.15)
elif service_level == 'bad':
    tip = float(total_bill * 0.1)

grand_total = float(total_bill + tip)
per_person = grand_total / split_check
per_person_text = 'Amount per person: '

print(tip_text + f'{tip: .2f}')
print(total + f'{grand_total:.2f}')
print(per_person_text + f'{per_person:.2f}')
