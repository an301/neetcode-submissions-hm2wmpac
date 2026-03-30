class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) == 3:
            if sum(nums) == 0:
                for num in nums:
                    res.append(num)
                return [res]
            else:
                return res

        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            num = nums[i]
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    
                    l += 1
                    r -= 1
            
        return res
                    
  
            
