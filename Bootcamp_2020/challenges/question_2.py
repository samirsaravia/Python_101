"""
Question 2
Write python code that will create a dictionary containing key, value pairs that
represent the first 12 values of the fibonacci sequence
"""
s = 12
a = 0
b = 1
d = dict()
for i in range(1, s + 1):
    d[i] = a
    a, b = b, b + a
print(d)
