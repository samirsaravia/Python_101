"""
Write a program that request five names separated by commas and create a
list containing those names. Print your answer.
For example: Samir, James, Alison, Tom, Sally
should return ['Samir','James','Alison','Tom','Sally']
"""
names = str(input('Names separated by commas: ')).strip().title()
list_names = names.split(',')
print(list_names)
