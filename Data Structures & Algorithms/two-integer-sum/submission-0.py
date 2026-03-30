class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = dict()
        for index, number in enumerate(nums):
            if target - number in pos:
                return [pos[target-number], index]
            pos[number] = index
        return -1