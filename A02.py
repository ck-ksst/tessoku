n, x = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for a in A:
    if a == x:
        print('Yes')
        exit()
print('No')

