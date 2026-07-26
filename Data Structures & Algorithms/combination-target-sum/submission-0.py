class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        currset = []
        self.helper(0, nums, target, result, currset)
        return result

    def helper(self, idx, nums, target, result, currset):
        if sum(currset) == target:
            result.append(currset[:])
            return 
        
        for i in range(idx, len(nums)):
            if sum(currset) > target:
                continue
            
            currset.append(nums[i])
            self.helper(i, nums, target, result, currset)
            currset.pop()
    