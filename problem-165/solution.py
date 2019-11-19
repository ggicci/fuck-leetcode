# Leetcode Problem #165 - Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        norm_length = max(len(v1), len(v2))
        v1.extend([0] * (norm_length - len(v1)))
        v2.extend([0] * (norm_length - len(v2)))

        for i in range(norm_length):
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1

        return 0
