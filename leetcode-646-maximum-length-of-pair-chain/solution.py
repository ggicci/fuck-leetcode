# Leetcode Problem
#  - id: 646
#  - title: Maximum Length of Pair Chain
#  - url: https://leetcode.com/problems/maximum-length-of-pair-chain/
#  - difficulty: medium

from bisect import bisect


class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        fronts = [x[0] for x in pairs]
        visited = [None] * len(pairs)
        for i in range(0, len(pairs)):
            self.dp(pairs, fronts, visited, i)

        return max(visited)

    def dp(self, pairs: List[List[int]], fronts: List[int], visited: List[int],
           i: int) -> int:
        if visited[i] is not None:
            return visited[i]

        _, high = pairs[i]
        at = bisect(fronts, high)
        sub_max = 0
        for j in range(at, len(pairs)):
            sub_max = max(sub_max, self.dp(pairs, fronts, visited, j))

        visited[i] = sub_max + 1
        return sub_max + 1
