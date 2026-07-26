class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        currset = []
        self.helper(1, currset, result, n, k)
        return result

    def helper(self, idx, currset, result, n, k):
        if len(currset) == k:
            result.append(currset[:])
            return
        if idx > n:
            return

        for i in range(idx, n+1):
            currset.append(i)
            self.helper(i + 1, currset, result, n, k)
            currset.pop()

    