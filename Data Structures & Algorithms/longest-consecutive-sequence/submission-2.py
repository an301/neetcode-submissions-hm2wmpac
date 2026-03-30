class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_ = 0
        for num in numSet:
            if num - 1 not in numSet:
                curr = 0
                while num + curr in numSet:
                    curr += 1
                    max_ = max(curr, max_)
        return max_
