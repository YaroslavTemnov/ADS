a, n, m = list(map(int, input().split()))
binary_power = bin(n)[:1:-1]
remainders = [a%m]
result = 1
if m == 1:
    result = 0
elif n == 0:
    result = 1
else:
    for i in range (len(binary_power)):
        remainders.append((remainders[-1]**2)%m)
    index = 0
    for i in binary_power:
        if i == "1":
            result = (result * remainders[index]) % m
            index +=1
        else:
            index += 1

print(result)