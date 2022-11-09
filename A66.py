class UnionFind:
    def __init__(self, n):
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x):
        while self.par[x] != -1:
            if self.par[x] == -1:
                break
            x = self.par[x]
        return x

    def unite(self, u, v):
        RootU = self.root(u)
        RootV = self.root(v)
        if RootU == RootV:
            return
        if self.size[RootU] < self.size[RootV]:
            self.par[RootU] = RootV
            self.size[RootV] += self.size[RootU]
        else:
            self.par[RootV] = RootU
            self.size[RootU] += self.size[RootV]

    def same(self, u, v):
        return self.root(u) == self.root(v)


n, q = map(int, input().split())
UF = UnionFind(n)
for _ in range(q):
    q, u, v = map(int, input().split())
    if q == 1:
        UF.unite(u, v)
    elif q == 2:
        if UF.same(u, v):
            print("Yes")
        else:
            print("No")
