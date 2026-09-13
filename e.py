def prime_searcher(primes):
    c = 1
    current_number = primes[-1] + c
    while True:
        current_number = primes[-1] + c
        for j in primes:
            if current_number % j == 0:
                break
            elif current_number % j != 0 and j == primes[-1]:
                c = 1
                return current_number

        c += 1

a = int(input())
b = a
primes_of_a = [1]
i = 0
primes = [2, 3, 5, 7, 9, 11, 13, 19, 23, 29]
while b != 1:
    if primes_of_a[-1] > a ** 0.5:
        primes_of_a.append(a)
        break
    elif primes[i] == primes[-1]:
        primes.append(prime_searcher(primes))
    else:
        if b % primes[i] == 0:
            b = b // primes[i]
            primes_of_a.append(primes[i])
            i = 0
        else:
            i += 1

for i in primes_of_a[1:]:
    print(i, end = " ")