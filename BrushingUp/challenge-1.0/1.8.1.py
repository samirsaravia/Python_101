# Write a function which prints the prime numbers in a given range


def prime(start: int, end: int):
    primes = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes


print(prime(3, 71))

# explains how it is calculated
# for i in range(10+1):
#     print(i, end=' ')
#     for j in range(2,i):
#         print(j,end=' ')
#     print()
