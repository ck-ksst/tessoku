n, m = map(int, input().split())
adj = [[] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b)
    adj[b - 1].append(a)
for i in range(n):
    print(f'{i + 1}: ', end='')
    print('{', end='')
    for j in range(len(adj[i])):
        if j >= 1:
            print(', ', end='')
        print(adj[i][j], end='')
    print('}')
