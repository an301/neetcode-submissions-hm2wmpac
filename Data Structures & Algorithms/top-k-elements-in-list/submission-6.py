import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 0
        #     freq[num] += 1

        # counts = []
        # for num in freq:
        #     counts.append((-freq[num], num))

        # heapq.heapify(counts)
        
        # out = []
        # for i in range(k):
        #     out.append(heapq.heappop(counts)[1])
        
        # return(out)

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        





