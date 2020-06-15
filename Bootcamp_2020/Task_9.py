"""
Question 9
    ******
    *
    *****
    *
    *
    *
Can you draw this using python?
"""
star = '*'
for i in range(0, 7):
    for j in range(0, 6):
        if i == 0 and j < 6:
            print(star, end='')
        elif i == 1 and j == 1:
            print()
            print(star)
        elif i == 2 and j < 5:
            print(star, end='')
        elif i == 3 and j == 3:
            print()
            print(star)
        elif i == 4 and j == 4:
            print(star)
        elif i == 5 and j == 5:
            print(star)
