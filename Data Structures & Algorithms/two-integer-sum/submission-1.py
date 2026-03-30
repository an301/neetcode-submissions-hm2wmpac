class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = dict()
        for idx, num in enumerate(nums):
            if target - num in pos:
                return [pos[target-num], idx]
            else:
                pos[num] = idx
        print(pos)