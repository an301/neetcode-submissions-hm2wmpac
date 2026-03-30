class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        while len(ans) != k:
            curr = ''
            max = 0
            for i in count:
                if count[i] > max:
                    max = count[i]
                    curr = i
            ans.append(curr)
            del count[curr]
        
        return(ans)