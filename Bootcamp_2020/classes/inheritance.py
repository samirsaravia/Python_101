class Patient(object):
    """
        Attributes
        ----------
        name: Patient name
        age:  Patient age
        conditions: existing medical conditions
    """
    status = 'patient'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self):
        print(f'{self.name},{self.age} years.'
              f'Current Condition: {self.conditions}')

    def add_info(self, information):
        self.conditions.append(information)


class Infant(Patient):
    """
        Attributes
        ----------
        name: infant name
        age: infant age
        vaccine: vaccines infant has had
    """
    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)

    def add_vac(self, vaccine):
        self.vaccinations.append(vaccine)

    def get_details(self):
        print(f'{self.name},{self.age} years.'
              f'\nPatient has had {self.vaccinations} vaccine.'
              f'\nCurrent information: {self.conditions}'
              f'\nPatient {self.name} is an INFANT, has he had all his checks?')


archie = Infant('Archie', 0)
archie.add_vac('MMA')
help(archie)
print(archie.get_details())

inher