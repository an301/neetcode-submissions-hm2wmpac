class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stk = []
        for i in nums:
            if i in stk:
                return True
            else:
                stk.append(i)
        return False
        