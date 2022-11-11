h, w, n = map(int, input().split())
imos = [[0] * (w + 2) for _ in range(h + 2)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    imos[a][b] += 1
    imos[a][d + 1] -= 1
    imos[c + 1][b] -= 1
    imos[c + 1][d + 1] += 1

s = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        s[i][j] = s[i][j - 1] + imos[i][j]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        s[i][j] = s[i - 1][j] + s[i][j]

for i in range(1, h + 1):
    print(*s[i][1:-1])
