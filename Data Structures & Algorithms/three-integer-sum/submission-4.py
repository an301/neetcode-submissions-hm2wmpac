class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i in range(len(nums)):
            l = nums[i]
            target = 0 - l
            j = i + 1
            r = len(nums) - 1
            if l in seen:
                continue
            seen.add(l)
            while j < r:
                if nums[j] + nums[r] == target:
                    if (l,nums[j],nums[r]) not in seen:
                        res.append([l,nums[j],nums[r]])
                        seen.add((l,nums[j],nums[r]))
                    j += 1
                elif nums[j] + nums[r] < target:
                    j += 1
                else:
                    r -= 1
        return res