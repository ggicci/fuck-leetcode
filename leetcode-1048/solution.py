# Leetcode Problem
#  - id: 1048
#  - title: Longest String Chain
#  - url: https://leetcode.com/problems/longest-string-chain/
#  - difficulty: medium


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0

        words.sort(key=len)
        cache = [1] * len(words)

        # Bottom-up dp.
        for i in range(len(words)):
            self.dp(words, cache, i)

        return max(cache)

    def is_predecessor(self, word_1: str, word_2: str) -> bool:
        """Test if word_1 is predecessor of word_2.
        """
        if len(word_1) + 1 != len(word_2):
            return False

        # Find the place where first make the difference.
        i = 0
        while i < len(word_1):
            if word_1[i] != word_2[i]:
                break
            i += 1
        # The remained part should be equal.
        while i < len(word_1):
            if word_1[i] != word_2[i + 1]:
                return False
            i += 1
        return True

    def dp(self, words: List[str], cache: List[int], i: int) -> int:
        if i == 0:
            return 1

        candidates = [1]
        for k in range(i - 1, -1, -1):
            if len(words[k]) + 1 < len(words[i]):
                break
            if self.is_predecessor(words[k], words[i]):
                candidates.append(cache[k] + 1)

        res = max(candidates)
        cache[i] = res
        return res
