class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = dict()
        for num in nums:
            if num not in dup:
                dup[num] = 0
            dup[num] += 1
            if dup[num] > 1:
                return True
        print(dup)
        return False