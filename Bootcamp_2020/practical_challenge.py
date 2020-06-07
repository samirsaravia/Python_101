"""
Ask the user for 2 numbers between 1 - 100. Then count from the lower number
to the higher number.print the result to the screen.
"""
while True:
    # additional code lines, error handling.
    try:
        n1 = int(input('Please digit a number between 1-100: '))
        n2 = int(input('Please digit a number between 1-100: '))
    except ValueError:
        print('please enter an integer.')
        continue
    else:
        while n1 < 0 or n2 < 0 or n1 > 100 or n2 > 100 or n1 == n2:
            print('Numbers must be different values between 1-100. Try again')
            n1 = int(input('Please digit a number between 1-100: '))
            n2 = int(input('Please digit a number between 1-100: '))
        if n1 < n2:
            for i in range(n1, n2 + 1):
                print(i, end=' ')
            break
        else:
            for i in range(n2, n1 + 1):
                print(i, end=' ')
            break
