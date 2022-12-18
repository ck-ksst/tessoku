def GCD(a, b):
    while a >= 1 and b >= 1:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a


# main #
a, b = map(int, input().split())
ans = GCD(a, b)
print(ans)
