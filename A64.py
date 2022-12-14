import heapq

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
INF = 10 ** 10

q = []
heapq.heapify(q)

cur = [INF] * (n + 1)
cur[1] = 0
kakutei = [False] * (n + 1)

heapq.heappush(q, (cur[1], 1))

while len(q) >= 1:
    pos = heapq.heappop(q)[1]
    if kakutei[pos] == True:
        continue

    kakutei[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(q, (cur[e[0]], e[0]))


for i in range(1, n + 1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print(-1)
