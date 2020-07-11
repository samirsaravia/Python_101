"""
Question 5
Create a dictionary containing as keys the letters from A-Z, the values should be random numbers created from the
random module. Can you draw a bar of the results.
"""
import matplotlib.pyplot as plt
import random
keys_number = dict()
keys = 'abcdefghijklmnopqrstuvwxyz'.upper()
for letter in keys:
    keys_number[letter] = random.randint(1, 100)
print(keys_number)
x, y = zip(*keys_number.items())
plt.bar(x, y)
plt.show()
