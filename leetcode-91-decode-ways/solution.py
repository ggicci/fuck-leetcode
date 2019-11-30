# Leetcode Problem
#  - id: 91
#  - title: Decode Ways
#  - url: https://leetcode.com/problems/decode-ways/
#  - difficulty: medium


class Solution:

    def numDecodings(self, s: str) -> int:
        cache = [None] * len(s)
        return self.num_decodings(s, 0, cache)

    def is_valid(self, s: str) -> bool:
        if not s:
            return False
        if s[0] == '0':
            return False
        code = int(s)
        if code < 1 or code > 26:
            return False
        return True

    def num_decodings(self, s: str, i: int, cache: List[int]) -> int:
        size = len(s) - i
        if size == 0 or s[i] == '0':
            return 0
        if size == 1:
            return 1

        ans = cache[i]
        if ans is not None:
            return ans

        ways = self.num_decodings(s, i + 1, cache)
        if self.is_valid(s[i:i + 2]):
            if size == 2:
                ways += 1
            else:
                ways += self.num_decodings(s, i + 2, cache)

        cache[i] = ways
        # print(f'cache[{i}]: {ways}')
        return ways
