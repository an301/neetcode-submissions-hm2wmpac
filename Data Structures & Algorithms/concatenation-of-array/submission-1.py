class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums.extend(nums)
        # return nums

        out = []
        for i in range(2):
            for num in nums:
                out.append(num)
        return out