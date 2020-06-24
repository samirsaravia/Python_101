from typing import Dict

countries: Dict[str, Dict[str, str]] = {'France': {'Capital': 'Paris', 'language': 'french'},
                                        'Spain': {'Capital': 'Madrid', 'language': 'Spanish'},
                                        'United Kingdom': {'Capital': 'London', 'language': 'English'},
                                        'Italy': {'Capital': 'Rome', 'language': 'italian'}}
for keys, values in countries.items():
    print(keys, values)
print()
for key, value in countries.items():
    print(f'{value["Capital"]} is the capital of {key}, they speak {value["language"]}')
