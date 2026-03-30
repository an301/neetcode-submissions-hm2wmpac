class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = {0:1}
        curr = 0
        res = 0
        for num in nums:
            curr += num
            if curr - k in prefs:
                res += prefs[curr-k]
            prefs[curr] = prefs.get(curr,0) + 1
        return res