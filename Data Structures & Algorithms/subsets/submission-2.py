class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = []

        # def backtrack(index, path):
        #     if index == len(nums):
        #         result.append(path[:])
        #         return
            
        #     path.append(nums[index])
        #     backtrack(index + 1, path)
        #     path.pop()

        #     backtrack(index + 1, path)
        
        # backtrack(0, [])
        # return result

        curset = []
        subset = []
        self.helper(0, nums, curset, subset)
        return subset

    def helper(self, idx, nums, curset, subset):
        if idx >= len(nums):
            subset.append(curset[:])
            return
        
        curset.append(nums[idx])
        self.helper(idx + 1, nums, curset, subset)
        curset.pop()

        self.helper(idx + 1, nums, curset, subset)
        

