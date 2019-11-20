# Leetcode Problem #22 - Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/


class Solution:

    def __init__(self):
        self.mem = {}

    def generateParenthesis(self, n: int) -> List[str]:
        return self.solve(n)

    def solve(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']

        if n in self.mem:
            return self.mem[n]

        candidates = set()
        for a in range(1, n):
            b = n - a
            a_sol = self.solve(a)
            b_sol = self.solve(b)
            for a_item in a_sol:
                for b_item in b_sol:
                    candidates.add(a_item + b_item)

        m_sol = self.solve(n - 1)
        for m_item in m_sol:
            candidates.add('(' + m_item + ')')

        res = list(candidates)
        self.mem[n] = res  # cache
        return res
