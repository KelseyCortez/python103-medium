# height and width for a triangle. prompt user for a height
height = int(input('Height? '))

width = (height * 2) - 1
triangle = ""

number_of_blanks = height - 1

for height_count in range(height):
    row = ""

for column_count in range(1, width + 1):
    if column_count <= number_of_blanks:
        row = row + " "
    elif column_count > (width - number_of_blanks):
        row = row + " "
    else:
        row = row + "*"
    
number_of_blanks = number_of_blanks - 1

triangle = triangle + row + "\n"

print(triangle)


