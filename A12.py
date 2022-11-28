n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))


def check(x):
    sum = 0
    for i in range(1, n + 1):
        sum += x // a[i]
    if sum >= k:
        return true
    else:
        return false
