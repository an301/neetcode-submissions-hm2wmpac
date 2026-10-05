class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        seen = set()
        min_heap = [(0,0)] #dist, idx
        n = len(points)

        while len(seen) < n:
            dist, idx = heapq.heappop(min_heap)

            if idx in seen:
                continue

            seen.add(idx)
            total += dist

            xi, yi = points[idx]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (dist, j))
        
        return total




        
