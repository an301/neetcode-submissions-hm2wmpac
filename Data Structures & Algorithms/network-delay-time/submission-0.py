class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        minHeap = [(0,k)]
        shortest = {}

        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        
        for val in times:
            source = val[0]
            target = val[1]
            time = val[2]
            adj[source].append((target, time))

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if node in shortest:
                continue

            shortest[node] = dist
            
            for nbr, time in adj[node]:
                if nbr not in shortest:
                    heapq.heappush(minHeap, (dist + time, nbr))

        
        if len(shortest) != n:
            return -1
        
        return max(shortest.values())
        


        
            


