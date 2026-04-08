class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        potential = float('inf')
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums and num - 1 > 0:
                if num - 1 < potential:
                    potential = num - 1
            if num + 1 not in nums and num + 1 > 0:
                if num + 1 < potential:
                    potential = num + 1

        if potential == float('inf'):
            return 1
        
        for i in range(potential-1, 0, -1):
            if i not in nums:
                potential = i

        return(potential)