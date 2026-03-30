import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        counts = []
        for num in freq:
            counts.append((-freq[num], num))

        heapq.heapify(counts)
        
        out = []
        for i in range(k):
            out.append(heapq.heappop(counts)[1])
        
        return(out)

        
        