import matplotlib.pyplot as plt
"""
Question 3
 Create a dictionary to represent the open, high, low, close share price data.
 For 4 imaginary companies 'Python DS', 'Python Soft', 'Pythazon' and 'Pybook'.

"""
companies = ['PythonDS', 'PythonSoft', 'Pythazon', 'Pybook']
key_names = ['open', 'high', 'low', 'close']
prices = [[12.52, 33.56, 16.5, 15.82], [13.56, 14.65, 16.65, 17.65], [21.66, 20.65, 24.56, 23.65],
          [12.56, 18.56, 8.56, 29.65]]
di = dict()
for i in range(len(key_names)):
    di[companies[i]] = dict(zip(key_names, prices[i]))
print(di)
di_high = {}
for i in di:
    di_high[i] = di[i]['high']
x, y = zip(*di_high.items())
plt.bar(x, y)
plt.show()
