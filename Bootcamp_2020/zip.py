list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
joined = list(zip(list_1, list_2))
print(f'The result of the zip function is {joined} and the type is {type(joined)}')
joined_1 = zip(list_1, list_2)
print(type(joined_1))
i, j = zip(*joined)
print(f'{i}\n{j}')
