# Leetcode Problem
#  - id: 935
#  - title: Knight Dialer
#  - url: https://leetcode.com/problems/knight-dialer/
#  - difficulty: medium


class Solution:
    MODULO = 10**9 + 7

    def __init__(self):
        self.candidates = (
            (4, 6),  # 0,
            (6, 8),  # 1,
            (7, 9),  # 2,
            (4, 8),  # 3,
            (3, 9, 0),  # 4,
            (),  # 5,
            (1, 7, 0),  # 6,
            (2, 6),  # 7,
            (1, 3),  # 8,
            (2, 4),  # 9,
        )

    def knightDialer(self, N: int) -> int:
        mem = [[None] * N for _ in range(10)]  # row=10, cols=N

        res = 0
        for k in range(10):
            res += self.dp(k, N - 1, mem)
        res %= self.MODULO
        return res

    def dp(self, k: int, n: int, mem: List[List[int]]) -> int:
        """Starts from k, makes n hops.
        """
        if n == 0:
            return 1
        if n == 1:
            return len(self.candidates[k])

        if mem[k][n] is not None:
            return mem[k][n]

        res = 0
        for x in self.candidates[k]:
            res += self.dp(x, n - 1, mem)

        # Memorize.
        res %= self.MODULO
        mem[k][n] = res
        return res
