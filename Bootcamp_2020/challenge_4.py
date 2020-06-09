"""
Question 4
Can you amend the solution to question 3 so that it just prints out
all times table between 1 and 12? No need to ask user for input
"""
print('==' * 15)
print('This is the 1-12 Times table')
print()
for i in range(1, 13):
    print('===' * 10)
    print(f'This is the {i} times table')
    for j in range(1, 13):
        print(f'{i} X {j} = {i * j}')
