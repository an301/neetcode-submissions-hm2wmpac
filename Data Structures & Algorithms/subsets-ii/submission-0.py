class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currset, subsets = [], []
        self.helper(0, nums, currset, subsets)
        return subsets

    def helper(self, idx, nums, currset, subsets):
        if idx == len(nums):
            subsets.append(currset[:])
            return
        
        currset.append(nums[idx])
        self.helper(idx + 1, nums, currset, subsets)
        currset.pop()

        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
        self.helper(idx + 1, nums, currset, subsets)