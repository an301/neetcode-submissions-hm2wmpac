class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(0, nums, target, result, 0, [])
        return result

    def helper(self, idx, nums, target, result, total, currset):
        if total == target:
            result.append(currset[:])
            return 
        
        if total > target:
            return 
        
        for i in range(idx, len(nums)):
            if total > target:
                continue
            
            currset.append(nums[i])
            self.helper(i, nums, target, result, total + nums[i], currset)
            currset.pop()
    