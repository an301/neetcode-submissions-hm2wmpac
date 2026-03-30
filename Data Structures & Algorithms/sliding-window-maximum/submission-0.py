class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums[:]
        
        n = len(nums)
        window_maximums = []
        dq = collections.deque()

        for i in range(n):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                window_maximums.append(nums[dq[0]])
        return window_maximums