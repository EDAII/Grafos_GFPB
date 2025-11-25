from typing import List
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        visitedCount = [0] * len(values)
        best = 0

        def dfs(node, timeSpent, currentSum):
            nonlocal best

            if node == 0:
                best = max(best, currentSum)

            for nei, cost in graph[node]:
                if timeSpent + cost > maxTime:
                    continue

                firstTime = visitedCount[nei] == 0
                if firstTime:
                    newSum = currentSum + values[nei]
                else:
                    newSum = currentSum

                visitedCount[nei] += 1
                dfs(nei, timeSpent + cost, newSum)
                visitedCount[nei] -= 1 

        visitedCount[0] = 1
        dfs(0, 0, values[0])

        return best
