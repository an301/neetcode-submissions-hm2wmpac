class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            lHeight = heights[left]
            rHeight = heights[right]
            diff = right - left
            if lHeight <= rHeight:
                area = diff * lHeight
                maxWater = max(area, maxWater)
                left += 1
            else:
                area = diff * rHeight
                maxWater = max(area, maxWater)
                right -= 1
        return maxWater