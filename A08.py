h, w = map(int, input().split())
x = [[0] * (w + 1)]

for _ in range(h):
    x.append([0] + list(map(int, input().split())))

q = int(input())
abcd = []
for _ in range(q):
    abcd.append(list(map(int, input().split())))

z = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        z[i][j] = z[i][j - 1] + x[i][j]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        z[i][j] = z[i - 1][j] + z[i][j]

for i in range(q):
    a, b, c, d = abcd[i]
    ans = z[c][d] + z[a - 1][b - 1] - z[c][b - 1] - z[a - 1][d]
    print(ans)
