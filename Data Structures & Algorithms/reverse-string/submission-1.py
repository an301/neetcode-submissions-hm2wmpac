class Solution:
    def reverseString(self, S: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(S) - 1
        while l < r:
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        