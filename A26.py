from math import sqrt, floor


def isPrime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# main
q = int(input())
ans = []
for _ in range(q):
    x = int(input())
    if isPrime(x):
        ans.append('Yes')
    else:
        ans.append('No')

for i in range(q):
    print(ans[i])
