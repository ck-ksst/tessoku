n, x = map(int, input().split())
a = list(map(int, input().split()))


def search(x):
    left = 0
    right = len(a) - 1
    while(left <= right):
        middle = (left + right) // 2
        if a[middle] < x:
            left = middle + 1
        elif a[middle] == x:
            return middle + 1
        else:
            right = middle - 1
    return -1


ans = search(x)
print(ans)
