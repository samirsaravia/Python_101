class Patient(object):
    """Medical center Patient"""
    status = 'patient'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self):
        print(f'Patient record: {self.name}, {self.age} years.\n'
              f'Current information: {self.conditions}')

    def add_info(self, information):
        self.conditions.append(information)


steven = Patient('steven Hack', 45)
steven.add_info('Treated for ear infection - amoxycilin prescribed')
print(steven.get_details())
abigail = Patient('Abigail', 32)
abigail.add_info(f'Treated for skin burn - ')
print(abigail.get_details())
