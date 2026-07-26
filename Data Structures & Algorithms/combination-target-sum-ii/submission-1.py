class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def helper(idx, curr, total):
            if total == target:
                result.append(curr[:])
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                helper(i + 1, curr, total + candidates[i])
                curr.pop()

        helper(0, [], 0)
        return result