class Solution:
    def reverseString(self, S: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(S) - 1
        while L <= R:
            S[L], S[R] = S[R], S[L]
            L += 1
            R -= 1
        