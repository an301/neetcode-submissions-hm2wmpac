class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArr = 0
        if len(heights) == 1:
            return heights[0]

        nextSmall = [-1] * len(heights)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if not stack:
                nextSmall[i] = len(heights)
            else:
                nextSmall[i] = stack[-1][1]
            stack.append((heights[i],i))
    
        prevSmall = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if not stack:
                prevSmall[i] = -1
            else:
                prevSmall[i] = stack[-1][1]
            stack.append((heights[i],i))

        for i in range(len(heights)):
            width = nextSmall[i] - prevSmall[i] - 1
            maxArr = max(maxArr, heights[i] * width)

        return maxArr