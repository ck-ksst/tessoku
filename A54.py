q = int(input())
score = {}
for _ in range(q):
    query = list(input().split())
    if query[0] == '1':
        x = query[1]
        y = int(query[2])
        score[x] = y
    else:
        x = query[1]
        print(score[x])
