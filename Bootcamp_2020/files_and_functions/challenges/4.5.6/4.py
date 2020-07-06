"""
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file in the same line
"""
file = open('capitals.txt', 'w+')
file.write('London, ')
file.write('Paris, ')
file.write('Madrid, ')
file.write('Rome, ')
file.write('Lisbon, ')
file.close()
with open('capitals.txt', 'r')as file:
    print(file.readline())
