# this program will prompt how many coins a user wants. it will print out current tally

How_many = input('Would you like a coin? ')
another = 'yes'
count = -1
while another == 'yes':
    count = count + 1
    print(f'You now have {count} coins! ')
    another = input('Would you like another? ').lower()
print('See ya! ')