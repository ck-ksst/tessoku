from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(1, m + 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0

d = deque()
d.append(1)
while len(d) >= 1:
    pos = d.popleft()
    for to in G[pos]:
        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            d.append(to)

for i in range(1, n + 1):
    print(dist[i])
