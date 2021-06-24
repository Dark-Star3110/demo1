
class disjiont_set:
    def __init__(self):
        self.pi = {}
        self.rank = {}

    def makeset(self, x):
        self.pi[x] = x
        self.rank[x] = 0

    def find (self, x):
        while x != self.pi[x]:
            x = self.pi[x]
        return x
    
    def union (self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            self.pi[ry] = rx
        else:
            self.pi[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] = self.rank[rx] + 1
