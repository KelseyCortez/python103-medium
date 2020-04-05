#given a height and width, print a box with * border

width = int(input('Width? '))
height = int(input('Height? '))


for i in range (width - 2):
    print('*' * width)
for i in range (height -2):
    print('*' * height)

print()