from collections import deque
q = int(input())
t = deque()
for _ in range(q):
    query = list(input().split())
    if query[0] == '1':
        t.append(query[1])
    elif query[0] == '2':
        print(t[0])
    elif query[0] == '3':
        t.popleft()
