class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                pref[i] = nums[i] * pref[i-1]
            else:
                pref[i] = nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1:
                post[i] = nums[i] * post[i+1]
            else:
                post[i] = nums[i]

        out = []
        for i in range(len(nums)):
            if i < 1:
                out.append(post[i+1])
            elif i == len(nums) - 1:
                out.append(pref[i-1])
            else:
                out.append(pref[i-1] * post[i+1])
        
        return(out)