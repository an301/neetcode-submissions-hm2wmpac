class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        max_ = 0
        for num in prices:
            if num < lowest:
                lowest = num
            else:
                max_ = max(max_, num - lowest)
        return max_