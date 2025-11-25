from typing import List
from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        
        secret = set([0, firstPerson])
        i = 0
        m = len(meetings)

        while i < m:
            time = meetings[i][2]
            group = []

            j = i
            while j < m and meetings[j][2] == time:
                x, y, t = meetings[j]
                group.append(x)
                group.append(y)
                j += 1

            group = list(set(group))

            idx = {p: k for k, p in enumerate(group)}

            dsu = DSU(len(group))

            for k in range(i, j):
                x, y, t = meetings[k]
                dsu.union(idx[x], idx[y])

            roots_with_secret = set()
            for p in group:
                if p in secret:
                    roots_with_secret.add(dsu.find(idx[p]))

            for p in group:
                if dsu.find(idx[p]) in roots_with_secret:
                    secret.add(p)

            i = j

        return list(secret)
