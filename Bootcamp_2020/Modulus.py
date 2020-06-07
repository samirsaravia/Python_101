n = 100
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
# sometimes range is much more memory efficient
print(list(range(10)))
print(list(range(1, 20, 2)))
print(type(range(10)))
