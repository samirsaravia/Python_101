class Patient(object):
    """Medical centre patient"""
    status = 'patient'

    def __init__(self, name, age):
        self.name = name
        self.age = age


steve = Patient('Steve Mawrick', 45)
abigail = Patient('Abigail Hughes', 32)
li = [1, 2, 3, 4, 1]
print(li.count(1))
