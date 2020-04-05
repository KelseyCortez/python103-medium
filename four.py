#given a height and width, print a box with * border

width = int(input('Width? '))
height = int(input('Height? '))

h = 0

while h < height:

    w = 0

while w < width:

    is_top = (h == 0)
    is_bottom = (h == (height - 1))
    is_left = (w == 0)
    is_right = (w == (width -1))

if is_top or is_bottom or is_left or is_right:
    print('*', end='')

else:
    print('  ', end='')

    h = h + 1
    w = w + 1
    