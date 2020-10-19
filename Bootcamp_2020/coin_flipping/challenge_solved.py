from math import sqrt

# Create a list with either heads or tails up
n = 1001
coins = [0] * n

# First loop increase step size, second one iterates through the coins
# swapping a 1 for 0 or 0 for 1.
# 1 = head / 0 = tail
for i in range(1, n):
    for j in range(0, n, i):
        coins[j] = 1 - coins[j]

# A dictionary contains all position of 'heads' swapped
d = {}
for i, v in enumerate(coins):
    if v != 0:
        d[i] = v


# A list appended just values or position of heads
L = []
for k, v in d.items():
    L.append(k)
print(f' List of Number-Heads {L}')
print()


# Displaying a pattern with math.sqrt
L2 = [sqrt(num) for num in L]
print(f'Square of Number-Heads'
      f'{L2}')
