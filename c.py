            
a = int(input())
nums= [i for i in range(0,a+1)]
nums[1] = 0
i = 2
while i <= a**0.5:
    if a % i == 0:
        nums[a] = 0
        break
    elif nums[i] != 0:
        j = i + i
        while j <= a:
            nums[j] = 0
            j = j + i
    i += 1

primes = set(nums)
primes.remove(0)
if a in primes:
    print("YES")
else:
    print("NO")