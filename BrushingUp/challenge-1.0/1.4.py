"""
Write some code that will return the numbers of CPUs in the system
"""
import psutil

# cpu count
cpu_count = psutil.cpu_count()
print(f'Number of CPUs: {cpu_count}')

# Can have the percentage of used RAM
print(psutil.virtual_memory().percent)

# You can convert object into a dictionary
dict_memo = dict(psutil.virtual_memory()._asdict())
print(dict_memo)

# calculate the percentage of available memory
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
