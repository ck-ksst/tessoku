n = int(input())
for i in range(9, -1, -1):
    wari = 1 << i
    print((n // wari) % 2, end='')
print('')
