from math import sqrt
N = 300000
q = int(input())
x = []
for _ in range(q):
    x.append(int(input()))

deleted = [False] * (N + 1)

for i in range(2, int(N ** 0.5) + 1):
    if deleted[i]:
        continue
    for j in range(i * 2, N + 1, i):
        deleted[j] = True

for i in range(q):
    if deleted[x[i]] == False:
        print('Yes')
    else:
        print('No')

