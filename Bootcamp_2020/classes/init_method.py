class Patient(object):
    """Medical center patient"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


steve = Patient('Steve Hugh', 48)
abigail = Patient('Abigail Sandwick', 32)
# It has now two-object python, each with its data(its own instances or variables)
print(steve.name)
print(steve.age)
print('--------')
print(abigail.name)
print(abigail.age)
