class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            elif midNum > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1