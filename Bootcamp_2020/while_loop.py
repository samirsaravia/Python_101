user_input = int(input('Please enter ages of class members. -1 to interrupt\n>>> '))
ages = []
while user_input > 0:
    ages.append(user_input)
    user_input = int(input('Next age: '))
print(f'The ages are {ages}')

# while loop plus counting
count = 0
class_names = []
name = input('Please entre a name ("n" to stop): ')
while name != 'n':
    count += 1
    class_names.append(name)
    print(f'{name} has been added')
    name = input('Next name: ')
print(f'There are {count} people in the class, they are: ')
print(class_names)
