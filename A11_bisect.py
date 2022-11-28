import bisect
n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = bisect.bisect_left(a, x) + 1
print(ans)
