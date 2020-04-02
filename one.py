# tip calculator total bill amount, level of service and bill amount plus tip amount total

bill = float(input('What is your total bill amount? '))

service = input('Was the level of service good, fair, or bad? ')

# print(service)
if service == 'good':
    tip = float(bill * 0.2)
    print("$%.2f" % tip)
elif service == 'fair':
    tip = float(bill * 0.15)
    print("$%.2f" % tip)
else:
    tip = float(bill * 0.1)
    print("$%.2f" % tip)

total = (bill + tip)

print("$%.2f" % total)

