class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(nums, i, memo):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            skip = helper(nums, i-1, memo)
            keep = helper(nums, i-2, memo) + nums[i]
            memo[i] = max(skip, keep)
            return memo[i]
        
        return helper(nums, len(nums)-1, memo)