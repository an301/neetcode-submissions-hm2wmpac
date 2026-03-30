import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        heap = []
        for i in nums:
            counts[i] = 1 + counts.get(i,0)
        
        for i in counts:
            heapq.heappush(heap, (-counts[i], i))

        top_k = []

        for i in range(k):
            num = heapq.heappop(heap)[1]
            top_k.append(num)
        
        return(top_k)