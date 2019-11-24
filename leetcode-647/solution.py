# Leetcode Problem
#  - id: 647
#  - title: Palindromic Substrings
#  - url: https://leetcode.com/problems/palindromic-substrings/
#  - difficulty: medium


class Solution:

    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for gap in range(1, len(s)):
            for i in range(len(s)):
                j = i + gap
                if j >= len(s):
                    continue
                if gap == 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                    continue
                dp[i][j] = 1 if s[i] == s[j] and dp[i + 1][j - 1] else 0

        return sum([sum(x) for x in dp])
