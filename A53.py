import heapq
q = int(input())
pq = []
heapq.heapify(pq)
for _ in range(q):
    query = list(input().split())
    if query[0] == '1':
        x = int(query[1])
        heapq.heappush(pq, x)
    elif query[0] == '2':
        print(pq[0])
    elif query[0] == '3':
        heapq.heappop(pq)
