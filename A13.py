n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
R = [0] * len(a)
ans = 0
for i in range(1, n + 1):
    if i == 1:
        R[i] = 1
    else:
        R[i] = R[i - 1]
    while R[i] < n and a[R[i] + 1] - a[i] <= k:
        R[i] += 1
ans = 0
for i in range(1, n):
    ans += R[i] - i
print(ans)
