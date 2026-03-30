class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            hleft = heights[left]
            hright = heights[right]
            dist = right - left
            if hleft < hright:
                area = hleft * dist
                maxArea = max(area, maxArea)
                left += 1
            else:
                area = hright * dist
                maxArea = max(area, maxArea)
                right -= 1
        return maxArea