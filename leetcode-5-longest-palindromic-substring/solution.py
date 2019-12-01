# Leetcode Problem
#  - id: 5
#  - title: Longest Palindromic Substring
#  - url: https://leetcode.com/problems/longest-palindromic-substring/
#  - difficulty: medium


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        mem = [[None] * len(s) for _ in range(len(s))]
        max_length = 0
        max_pos = (0, 0)
        for i in range(len(s)):
            for j in range(i, len(s)):
                self.palindrome(s, i, j, mem)
                if mem[i][j] is True:
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        max_pos = (i, j)
        return s[max_pos[0]:max_pos[1] + 1]

    def palindrome(self, s: str, i: int, j: int, mem: List[List[int]]) -> bool:
        """
        Returns the size of substring s[i...j] when the substring is palindrome,
        otherwise 0.
        """
        is_palindrome = mem[i][j]
        if is_palindrome is not None:
            return is_palindrome

        if i > j:
            mem[i][j] = False
            return False
        if i == j:
            mem[i][j] = True
            return True

        if i + 1 == j:  # of size 2
            is_palindrome = s[i] == s[j]
            mem[i][j] = is_palindrome
            return is_palindrome

        is_palindrome = s[i] == s[j] and self.palindrome(s, i + 1, j - 1, mem)
        mem[i][j] = is_palindrome
        return is_palindrome
