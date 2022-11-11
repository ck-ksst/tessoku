d = int(input())
n = int(input())
imos = [0] * (d + 2)
for _ in range(n):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r + 1] -= 1
ans = [0] * (d + 2)
for i in range(1, d + 1):
    ans[i] = ans[i - 1] + imos[i]
    print(ans[i])
