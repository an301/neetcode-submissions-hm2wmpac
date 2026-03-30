class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > (len(nums) // 3):
                res.add(num)
        return list(res)