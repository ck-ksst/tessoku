n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
l = []
r = []
for _ in range(q):
    l_, r_ = map(int, input().split())
    l.append(l_)
    r.append(r_)

for i in range(q):
    print(s[r[i]] - s[l[i] - 1])
