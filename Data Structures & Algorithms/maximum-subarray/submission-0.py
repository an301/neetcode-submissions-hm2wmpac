class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        curr = 0

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            max_ = max(max_, curr)
        
        return max_