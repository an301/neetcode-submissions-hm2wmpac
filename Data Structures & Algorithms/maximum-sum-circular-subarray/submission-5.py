class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = nums[0]
        globMax = nums[0]

        currMin = nums[0]
        globMin = nums[0]

        total = nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            globMax = max(globMax, currMax)

            currMin = min(nums[i], currMin + nums[i])
            globMin = min(globMin, currMin)

            total += nums[i]
        
        if globMax < 0:
            print(1)
            return globMax
        
        if total - globMin > globMax:
            print(2)
            print(total, globMin, globMax)
            return total-globMin
        
        print(3)
        return globMax

                