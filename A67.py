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


n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

uf = UnionFind(n)
ans = 0
for a, b, c in edges:
    if not uf.same(a, b):
        uf.unite(a, b)
        ans += c

print(ans)
