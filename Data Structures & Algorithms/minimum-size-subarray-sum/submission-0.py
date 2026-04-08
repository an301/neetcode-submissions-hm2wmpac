class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        state = 0
        minLen = float('inf')
        start = 0

        for end in range(len(nums)):
            state += nums[end]

            while state >= target:
                minLen = min(minLen, end - start + 1)
                state -= nums[start]
                start += 1
        
        if minLen == float('inf'):
            return 0
        return minLen

