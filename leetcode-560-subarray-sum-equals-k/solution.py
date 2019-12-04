# Leetcode Problem
#  - id: 560
#  - title: Subarray Sum Equals K
#  - url: https://leetcode.com/problems/subarray-sum-equals-k/
#  - difficulty: medium


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        # {sum: count}
        seen = {0: 1}
        s = 0
        counter = 0
        for i in range(len(nums)):
            s += nums[i]
            delta = s - k
            if delta in seen:
                counter += seen.get(delta, 0)
            seen[s] = seen.get(s, 0) + 1

        return counter
