# Leetcode Problem #17 - Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    KEYBOARD = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }

    def __init__(self):
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.bt(digits, 0, [])
        return self.res

    def bt(self, digits: str, index: int, path: List[str]):
        if index == len(digits):
            self.res.append(''.join(path))
            return

        digit = digits[index]
        for cand in self.KEYBOARD[digit]:
            self.bt(digits, index + 1, path + [cand])
