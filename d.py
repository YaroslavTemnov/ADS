a = int(input())
primes = [2]
c = 1
while len(primes) != a:
    j = (primes[-1]+c)
    for i in primes:
        if j % i == 0:
            break
        elif i == primes[-1] and j % i != 0:
            primes.append(j)
            c = 1
            break

    c += 1
print(primes[-1])