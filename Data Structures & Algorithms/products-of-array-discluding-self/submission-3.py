class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        for i in range(len(nums)):
            if i == 0:
                pref.append(nums[i])
            else:
                pref.append(pref[i-1] * nums[i])
        
        post = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post[i] = nums[i]
            else:
                post[i] = post[i + 1] * nums[i]
        
        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(post[i+1])
            elif i == len(nums) - 1:
                out.append(pref[i-1])
            else:
                out.append(post[i+1] * pref[i-1])

        return out