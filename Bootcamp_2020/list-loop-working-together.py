data = [2, 14, 10, 22, 45, 98, 15, 54]
data_copy = data[:]
for i in range(len(data_copy)):
    for j in range(0, len(data_copy) - i - 1):
        if data_copy[j] > data_copy[j + 1]:
            # here switch the values using bubble sort
            data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
            print(data_copy[j], data_copy[j + 1])
print(f'Original {data}')
print(f'Ordenado usando bolha se troca {data_copy}')
print(f'ordenado usando def do python {sorted(data)}')
data.extend([3, 12, 44, 30])
print(data)