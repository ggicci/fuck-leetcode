# Leetcode Problem #1130 - Minimum Cost Tree From Leaf Values
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/submissions/


class Solution:

    def __init__(self):
        self.mem = {}

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0
        return self.dp(arr, 0, len(arr) - 1)[1]

    def dp(self, arr: List[int], s: int, e: int) -> tuple:
        """Find optimized result of arr[s:e+1], i.e. [s, e].

        Returns:
            max_of_subtree: The maxinum value in [s,e] range.
            minimum_cost: Minimum cost tree sum.
        """
        if s == e:  # 1 node
            return (arr[s], 0)

        key = (s, e)
        if key in self.mem:
            return self.mem[key]

        if e - s == 1:  # 2 nodes
            res = (max(arr[s], arr[e]), arr[s] * arr[e])
        else:
            costs = []
            for k in range(s, e):
                left_max, left_cost = self.dp(arr, s, k)
                right_max, right_cost = self.dp(arr, k + 1, e)
                costs.append(left_cost + right_cost + left_max * right_max)
            res = (max(arr[s:e + 1]), min(costs))

        self.mem[key] = res
        # print(f'key: {key}, value: {res}')
        return res
